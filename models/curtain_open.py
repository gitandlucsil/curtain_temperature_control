from .controltypes import Types
from .curtain import Curtain

class CurtainOpen(object):

    def __init__(self):
        self._cal = 19.5
        self._cad = 19.0
        self._ton = 40
        self._toff = 180
        self._state = Types.CA_INITIAL_STATE
        self._time = 0
        self._curtain = Curtain()

    @property
    def cal(self):
        return self._cal

    @cal.setter
    def cal(self, value):
        self._cal = float(value)
        print("CurtainOpen - Changed cal to ",self._cal)

    @property
    def cad(self):
        return self._cad

    @cad.setter
    def cad(self, value):
        self._cad = float(value)
        print("CurtainOpen - Changed cad to ",self._cad)

    @property
    def ton(self):
        return self._ton

    @ton.setter
    def ton(self, value):
        self._ton = int(value)
        print("CurtainOpen - Changed ton to ",self._ton)

    @property
    def toff(self):
        return self._toff

    @toff.setter
    def toff(self, value):
        self._toff = int(value)
        print("CurtainOpen - Changed toff to ",self._toff)

    @property 
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        print("CurtainOpen - Changed state to",self._state)

    def fsm(self):
        if self._state == Types.CA_INITIAL_STATE:
            self._state = Types.CA_OPENNING
            print("CurtainOpen - Start to open!")
            self._time = 0
            self._curtain.status = Types.OPENING
        elif self._state == Types.CA_OPENNING:
            print("CurtainOpen - Openning!")
            self._time += 1
            print("CurtainOpen - Passed %s seconds" % self._time)
            self._curtain.abertura += 1
            if self._time >= self._ton:
                self._state = Types.CA_STOPPED
                self._time = 0
                self._curtain.status = Types.STOPPED
        elif self._state == Types.CA_STOPPED:
            print("CurtainOpen - Waiting!")
            self._time += 1
            print("CurtainOpen - Passed %s seconds" % self._time)
            if self._time >= self._toff:
                self._state = Types.CA_INITIAL_STATE
