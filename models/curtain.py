class Curtain(object):

    def __init__(self):
        self._abertura = 30

    @property
    def abertura(self):
        return self._abertura

    @abertura.setter
    def abertura(self, value):
        self._abertura = int(value)
        print("Curtain - Changed abertura to ",self._abertura)

