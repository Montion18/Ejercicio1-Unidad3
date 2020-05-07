
class capitulos:
    __titulo=''
    __cantpag=0

    def __init__(self,titulo,cantp):
        self.__titulo=titulo
        self.__cantpag=cantp

    def gettitulo(self):
        return self.__titulo
    def getpag(self):
        return self.__cantpag