class CurtainClose(object):

    def __init__(self):
        self._cfl = 18.5
        self._cfd = 19.0
        self._ton = 40
        self._toff = 180

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