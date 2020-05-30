class CurtainOpen(object):

    def __init__(self):
        self._cal = 19.5
        self._cad = 19.0
        self._ton = 40
        self.t_off = 180

    @property
    def cal(self):
        return self._cal

    @cal.setter
    def cal(self, value):
        self._cal = float(value)