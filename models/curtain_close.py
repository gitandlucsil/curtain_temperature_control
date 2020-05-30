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

    @property
    def cfd(self):
        return self._cfd

    @cfd.setter
    def cfd(self, value):
        self._cfd = float(value)

    @property
    def ton(self):
        return self._ton

    @ton.setter
    def ton(self, value):
        self._ton = int(value)

    @property
    def toff(self):
        return self._toff

    @toff.setter
    def toff(self, value):
        self._toff = int(value)