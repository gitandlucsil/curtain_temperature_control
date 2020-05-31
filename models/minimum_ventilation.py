from .controltypes import Types
from .curtain import Curtain

class MinimunVentilation(object):

    def __init__(self):
        self._abrefecha = 30
        self._aberto = 40
        self._fechado = 180
        self._limite = 30
        self._state = Types.VM_INITIAL_STATE
        self._time = 0
        self._curtain = Curtain()

    @property
    def abrefecha(self):
        return self._abrefecha

    @abrefecha.setter
    def abrefecha(self, value):
        self._abrefecha = int(value)
        print("MinimunVentilation - Changed abrefecha to ",self._abrefecha)

    @property
    def aberto(self):
        return self._aberto

    @aberto.setter
    def aberto(self, value):
        self._aberto = int(value)
        print("MinimunVentilation - Changed aberto to ",self._aberto)

    @property
    def fechado(self):
        return self._fechado

    @fechado.setter
    def fechado(self, value):
        self._fechado = int(value)
        print("MinimunVentilation - Changed fechado to ",self._fechado)

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, value):
        self._limite = int(value)
        print("MinimunVentilation - Changed limite to ",self._limite)

    @property 
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        print("MinimunVentilation - Changed state to",self._state)

    def fsm(self):
        if self._state == Types.VM_INITIAL_STATE:
            print("MinimunVentilation - Start to open!")
            self._state = Types.VM_OPENING
            self._time = 0
            self._curtain.status = Types.OPENING
        elif self._state == Types.VM_OPENING:
            print("MinimunVentilation - Opening!")
            self._time += 1
            print("MinimunVentilation - Passed %s seconds" % self._time)
            self._curtain.abertura += 1
            if self._time >= self._abrefecha:
                self._state = Types.VM_WAIT_OPEN
                self._time = 0
                self._curtain.status = Types.STOPPED
        elif self._state == Types.VM_WAIT_OPEN:
            print("MinimunVentilation - Waiting openned!")
            self._time += 1
            print("MinimunVentilation - Passed %s seconds" % self._time)
            if self._time >= self._aberto:
                self._state = Types.VM_CLOSING
                self._time = 0
                self._curtain.status = Types.CLOSING
        elif self._state == Types.VM_CLOSING:
            print("MinimunVentilation - Closing!")
            self._time += 1
            print("MinimunVentilation - Passed %s seconds" % self._time)
            self._curtain.abertura -= 1
            if self._time >= self._abrefecha:
                self._state = Types.VM_WAIT_CLOSING
                self._time = 0
                self._curtain.status = Types.STOPPED
        elif self._state == Types.VM_WAIT_CLOSING:
            print("MinimunVentilation - Waiting closed!")
            self._time += 1
            print("MinimunVentilation - Passed %s seconds" % self._time)
            if self._time >= self._fechado:
                self._state = Types.VM_INITIAL_STATE
                self._time = 0
                self._curtain.status = Types.STOPPED
