class CurtainOpen(object):

    def __init__(self):
        self._cal = 19.5
        self._cad = 19.0
        self._ton = 40
        self._toff = 180

    @property
    def cal(self):
        return self._cal

    @cal.setter
    def cal(self, value):
        self._cal = float(value)

    @property
    def cad(self):
        return self._cad

    @cad.setter
    def cad(self, value):
        self._cad = float(value)

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