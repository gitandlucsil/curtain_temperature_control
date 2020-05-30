import sys
import os
import gevent
import redis
from gevent import monkey
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
            if self._temperature >= self._ca.cal:
                print("abre cortina")
            else:
                if self._temperature <= self._ca.cad:
                    print("parou de abrir a cortina!")
                    if self._curtain.abertura < self._vm.limite:
                        print("ventilação mínima")
                    else:
                        if self._temperature <= self._cf.cfl:
                            print("fechar_cortina")
                        elif self._temperature >= self._cf.cfd:
                            print("parou de fechar cortina")
                
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