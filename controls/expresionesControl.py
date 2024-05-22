from models.expresiones import Expresiones
from controls.tda.linked.linkedList import Linked_List

class ExpresionesControl:
    def __init__(self):
        self.__expresiones = None
        self.__id_counter = 0
        self.__lista = Linked_List()
        
    @property
    def _expresiones(self):
        if self.__expresiones == None:
            self.__expresiones = Expresiones()
        return self.__expresiones

    @_expresiones.setter
    def _expresiones(self, value):
        self.__expresiones = value
        
    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value 
    
    def save(self):
        self._expresiones._id = self.__id_counter
        self._lista.add(self._expresiones, self._lista._lenght)
        
    def eliminar(self, pos):
        self._lista.delete(pos)

    