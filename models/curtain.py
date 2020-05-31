from .singleton import singleton
from .controltypes import Types

@singleton
class Curtain(object):

    def __init__(self):
        self._abertura = 0
        self._status = Types.STOPPED
        self._control = Types.NONE

    @property
    def abertura(self):
        return self._abertura

    @abertura.setter
    def abertura(self, value):
        if int(value) >= 100:
            value = 100
        elif int(value) <= 0:
            value = 0
        self._abertura = int(value)
        print("Curtain - Changed abertura to ",self._abertura)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def control(self):
        return self._control

    @control.setter
    def control(self, value):
        self._control = value


