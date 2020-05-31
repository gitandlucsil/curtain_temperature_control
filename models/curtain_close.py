from .controltypes import Types
from .curtain import Curtain

class CurtainClose(object):

    def __init__(self):
        self._cfl = 18.5
        self._cfd = 19.0
        self._ton = 40
        self._toff = 180
        self._state = Types.CF_INITIAL_STATE
        self._time = 0
        self._curtain = Curtain()

    @property
    def cfl(self):
        return self._cfl

    @cfl.setter
    def cfl(self, value):
        self._cfl = float(value)
        print("CurtainClose - Changed cfl to ",self._cfl)

    @property
    def cfd(self):
        return self._cfd

    @cfd.setter
    def cfd(self, value):
        self._cfd = float(value)
        print("CurtainClose - Changed cfd to ",self._cfd)

    @property
    def ton(self):
        return self._ton

    @ton.setter
    def ton(self, value):
        self._ton = int(value)
        print("CurtainClose - Changed ton to ",self._ton)

    @property
    def toff(self):
        return self._toff

    @toff.setter
    def toff(self, value):
        self._toff = int(value)
        print("CurtainClose - Changed toff to ",self._ton)

    @property 
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        print("CurtainClose - Changed state to",self._state)

    def fsm(self):
        if self._state == Types.CF_INITIAL_STATE:
            self._state = Types.CF_CLOSING
            print("CurtainClose - Start to close!")
            self._time = 0
            self._curtain.status = Types.CLOSING
        elif self._state == Types.CF_CLOSING:
            print("CurtainClose - Closing!")
            self._time += 1
            print("CurtainClose - Passed %s seconds" % self._time)
            self._curtain.abertura -= 1
            if self._time >= self._ton:
                self._state = Types.CF_STOPPED
                self._time = 0
                self._curtain.status = Types.STOPPED
        elif self._state == Types.CF_STOPPED:
            print("CurtainClose - Waiting!")
            self._time += 1
            print("CurtainClose - Passed %s seconds" % self._time)
            if self._time >= self._toff:
                self._state = Types.CF_INITIAL_STATE