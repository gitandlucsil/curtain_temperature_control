class MinimunVentilation(object):

    def __init__(self):
        self._abrefecha = 30
        self._aberto = 40
        self._fechado = 180
        self._limite = 30

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