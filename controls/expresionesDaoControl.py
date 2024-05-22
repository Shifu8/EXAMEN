from controls.dao.daoAdapter import DaoAdapter
from models.expresiones import Expresiones

class ExpresionesDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Expresiones)
        self.__expresiones = None

    @property
    def _expresiones(self):
        if self.__expresiones == None:
            self.__expresiones = Expresiones()   
        return self.__expresiones

    @_expresiones.setter
    def _expresiones(self, value):
        self.__expresiones = value

    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._expresiones._id = self._lista + 1
        self._save(self._expresiones)
    
    def merge(self, pos):
        self._merge(self._expresiones, pos)