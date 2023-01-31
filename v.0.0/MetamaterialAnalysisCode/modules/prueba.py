class calse_prueba:
    def __init__(self):
        self.__a = 1
        self.__b = 2

    def set_a(self, a):
        self.__a = a
    
    def set_b(self, b):
        self.__b = b

    def suma(self):
        return self.__a + self.__b

    def resta(self):
        return self.__a - self.__b

    def multiplicacion(self):
        return self.__a * self.__b

    def division(self):
        return self.__a / self.__b