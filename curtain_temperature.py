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
            print("running!")
            gevent.sleep(1)

    def publisher(self, channel, value):
        self._redis.set(str(channel),str(value))
        self._redis.publish(str(channel),str(value))

    def subscriber(self):
        print("subscriber")
        pubsub = self._redis.pubsub(ignore_subscribe_messages=True)
        pubsub.subscribe("cal")
        pubsub.subscribe("cad")
        pubsub.subscribe("cfd")
        pubsub.subscribe("cfl")
        
        for notification in pubsub.listen():
            if notification["channel"] == "cal":
                pass
            elif notification["channel"] == "cad":
                pass
            elif notification["channel"] == "cfl":
                pass
            elif notification["channel"] == "cfd":
                pass


def main():
    temperatureCurtainControl = TemperatureCurtainControl()
    greenlets.append(gevent.spawn(temperatureCurtainControl.subscriber))
    greenlets.append(gevent.spawn(temperatureCurtainControl.run))
    gevent.joinall(greenlets)

if __name__ == "__main__":
    main()