class Expresiones:
    def __init__(self):
        self.__id = 0
        self.__expresionObtenida = ''
        self.__numero1 = 0
        self.__numero2 = 0
        self.__operando1 = ''
        self.__operando2 = ''
        self.__resultado = 0.0

    @property
    def _operando1(self):
        return self.__operando1

    @_operando1.setter
    def _operando1(self, value):
        self.__operando1 = value

    @property
    def _operando2(self):
        return self.__operando2

    @_operando2.setter
    def _operando2(self, value):
        self.__operando2 = value

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _expresionObtenida(self):
        return self.__expresionObtenida

    @_expresionObtenida.setter
    def _expresionObtenida(self, value):
        self.__expresionObtenida = value

    @property
    def _numero1(self):
        return self.__numero1

    @_numero1.setter
    def _numero1(self, value):
        self.__numero1 = value

    @property
    def _numero2(self):
        return self.__numero2

    @_numero2.setter
    def _numero2(self, value):
        self.__numero2 = value


    @property
    def _resultado(self):
        return self.__resultado

    @_resultado.setter
    def _resultado(self, value):
        self.__resultado = value

        
    @property
    def serializable(self):
        return {
            "id": self.__id,
            "expresion": self.__expresionObtenida,
            "numero1": self.__numero1,
            "numero2": self.__numero2,
            "operando1": self.__operando1,
            "operando2": self.__operando2,
            "resultado": self.__resultado
        }
    
    def deserializar(data):
        expresion = Expresiones()
        expresion._id = data["id"]
        expresion._expresionObtenida = data["expresionObtenida"]
        expresion._numero1 = data["numero1"]
        expresion._numero2 = data["numero2"] 
        expresion._resultado = data["resultado"]
        return expresion
    
    def __str__(self):
        return f"ID: {self._id}, expresion Obtenida: {self._expresionObtenida}, Numero 1: {self._numero1}, Numero 2: {self._numero2}, Operando: {self._operando}, resultado: {self._resultado}"
