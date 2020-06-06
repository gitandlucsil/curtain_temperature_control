import sys
import os
import gevent
import redis
from gevent import monkey
from models.controltypes import Types
from models.curtain_open import CurtainOpen
from models.curtain_close import CurtainClose
from models.minimum_ventilation import MinimunVentilation
from models.curtain import Curtain

monkey.patch_socket()
greenlets = []

class TemperatureCurtainControl(object):
    
    REDIS_CONFIG = {
        "host" : "localhost",
        "port" : 6379,
        "db" : 0,
        "decode_responses" : True,
    }

    def __init__(self):
        print("Just started!")
        self._ca = CurtainOpen()
        self._cf = CurtainClose()
        self._vm = MinimunVentilation()
        self._curtain = Curtain()
        self._temperature = 19
        self._started_cf_by_vm = False
        self._redis = redis.StrictRedis(**TemperatureCurtainControl.REDIS_CONFIG)

        if not self._is_registered('system.services','temperaturecurtaincontrol'):
            self._redis.append('system.services','temperaturecurtaincontrol')

    def _is_registered(self, channel, value):
        list = self._redis.get(channel)
        if list:
            items = list.split(' ')
            for item in items:
                if item == value:
                    return True
        return False  

    def run(self):
        while True:
            if self._temperature >= self._ca.cal: #Se a Temperatura ficar acima do CAL
                if self._curtain.control != Types.CA: #Passa o controle para abertura de cortina
                    self._curtain.control = Types.CA
            else: #Caso a temperatura ficar abaixo de CAL
                if self._temperature <= self._ca.cad: #Se a Temperatura cair o CAD
                    if self._curtain.control == Types.CA: #Se o contrile estiver para abertura da cortina
                        self._ca.state = Types.CA_INITIAL_STATE #Para de abrir a cortina
                        self._curtain.control = Types.NONE
                    if self._curtain.abertura < self._vm.limite: #Se a abertura for menor que o Limite da VM
                        if self._curtain.control == Types.CF: #Estiver controlando por CF
                            if (self._cf.state == Types.CF_INITIAL_STATE) or (self._cf.state == Types.CF_STOPPED):
                                self._curtain.control = Types.VM #Se estiver com a CF parada, retorna para VM
                        else: #Caso contrario, retornar o controle para VM
                            if self._curtain.control != Types.VM:
                                self._curtain.control = Types.VM
                    else: #Se a abertura for maior ou igual que o Limite da VM
                        if self._curtain.control != Types.VM: #Se não estiver controlando por VM
                            if self._temperature <= self._cf.cfl: #Se a Temperatura ficar abaixo de CFL
                                if self._curtain.control != Types.CF:
                                    self._curtain.control = Types.CF
                            elif self._temperature >= self._cf.cfd: #Se a Temperatura subir o CFD
                                if self._curtain.control == Types.CF:
                                    self._cf.state = Types.CF_INITIAL_STATE
                                    self._curtain.control = Types.NONE
                        if self._vm.state == Types.VM_WAIT_CLOSING: #Se estiver no estado de espera fechado da VM, sai do controle
                            self._curtain.control = Types.NONE
                else:
                    if self._curtain.control == Types.CF: #Estiver controlando por CF
                        if self._temperature >= self._cf.cfd: #Se a Temperatura subir o CFD
                            self._cf.state = Types.CF_INITIAL_STATE
                            self._curtain.control = Types.NONE
                    if self._temperature >= self._ca.cad:
                        if((self._curtain.control != Types.CF) and (self._curtain.control != Types.CA)):
                            if self._curtain.abertura < self._vm.limite:
                                self._curtain.control = Types.VM
            if self._curtain.control == Types.CA:
                self._vm.state = Types.VM_INITIAL_STATE
                self._cf.state = Types.CF_INITIAL_STATE
                self._ca.fsm()
            elif self._curtain.control == Types.CF:
                self._vm.state = Types.VM_INITIAL_STATE
                self._ca.state = Types.CA_INITIAL_STATE
                self._cf.fsm()
            elif self._curtain.control == Types.VM:
                self._ca.state = Types.CA_INITIAL_STATE
                self._vm.fsm()
                if self._vm.state == Types.VM_WAIT_CLOSING: #No tempo de espera fechado da VM
                    if (self._temperature <= self._cf.cfl) and (self._started_cf_by_vm is False): #Se a Temperatura ficar abaixo de CFL
                        self._cf.fsm()
                        self._started_cf_by_vm = True
                    if (self._temperature < self._cf.cfd) and (self._started_cf_by_vm is True):
                        self._cf.fsm()
                    if self._temperature >= self._cf.cfd:
                        self._started_cf_by_vm = False
                        self._cf.state = Types.CF_INITIAL_STATE
                else:
                    self._cf.state = Types.CF_INITIAL_STATE
            elif self._curtain.control == Types.NONE:
                self._ca.state = Types.CA_INITIAL_STATE
                self._cf.state = Types.CF_INITIAL_STATE
                self._vm.state = Types.VM_INITIAL_STATE
            self.publisher("abertura",self._curtain.abertura)
            gevent.sleep(1)

    def publisher(self, channel, value):
        self._redis.set(str(channel),str(value))
        self._redis.publish(str(channel),str(value))

    def subscriber(self):
        print("subscriber")
        pubsub = self._redis.pubsub(ignore_subscribe_messages=True)
        pubsub.subscribe("temperature")
        pubsub.subscribe("cal")
        pubsub.subscribe("cad")
        pubsub.subscribe("ca_ton")
        pubsub.subscribe("ca_toff")
        pubsub.subscribe("cfl")
        pubsub.subscribe("cfd")
        pubsub.subscribe("cf_ton")
        pubsub.subscribe("cf_toff")
        pubsub.subscribe("abrefecha")
        pubsub.subscribe("aberto")
        pubsub.subscribe("fechado")
        pubsub.subscribe("limite")
        pubsub.subscribe("abertura")
        
        for notification in pubsub.listen():
            if notification["channel"] == "temperature":
                self._temperature = float(notification["data"])
            elif notification["channel"] == "cal":
                self._ca.cal = notification["data"]
            elif notification["channel"] == "cad":
                self._ca.cad = notification["data"]
            elif notification["channel"] == "ca_ton":
                self._ca.ton = notification["data"]
            elif notification["channel"] == "ca_toff":
                self._ca.toff = notification["data"]
            elif notification["channel"] == "cfl":
                self._cf.cfl = notification["data"]
            elif notification["channel"] == "cfd":
                self._cf.cfd = notification["data"]
            elif notification["channel"] == "cf_ton":
                self._cf.ton = notification["data"]
            elif notification["channel"] == "cf_toff":
                self._cf.toff = notification["data"]
            elif notification["channel"] == "abrefecha":
                self._vm.abrefecha = notification["data"]
            elif notification["channel"] == "aberto":
                self._vm.aberto = notification["data"]
            elif notification["channel"] == "fechado":
                self._vm.fechado = notification["data"]
            elif notification["channel"] == "limite":
                self._vm.limite = notification["data"]
            elif notification["channel"] == "abertura":
                self._curtain.abertura = notification["data"]

def main():
    temperatureCurtainControl = TemperatureCurtainControl()
    greenlets.append(gevent.spawn(temperatureCurtainControl.subscriber))
    greenlets.append(gevent.spawn(temperatureCurtainControl.run))
    gevent.joinall(greenlets)

if __name__ == "__main__":
    main()