
class libro:
    __id=0
    __titulo=''
    __autor=''
    __editorial=''
    __isbn=0
    __cantcap=0
    __cap=[]

    def __init__(self,id,tit,autor,edit,isbn,cantc):
        self.__id=id
        self.__titulo=tit
        self.__autor=autor
        self.__editorial=edit
        self.__isbn=isbn
        self.__cantcap=cantc
    def setcapitulo(self,cap):
        self.__cap.append(cap)
        pass
    def getid(self):
        return self.__id
    def getaut(self):
        return self.__autor
    def gettit(self):
        return self.__titulo
    def gettotalpag(self):
        total=0
        for i in range(self.__cantcap):
            total=total+int(self.__cap[i].getpag())
        return total
    def getnombcap(self):
        for i in range(self.__cantcap):
            print("\nNombre del capitulo:",self.__cap[i].gettitulo())
    def buscacapitulos(self,palabra):
        for j in range(self.__cantcap):
            if self.__cap[j].gettitulo().find(palabra)>=0:
                return 1
            if j==self.__cantcap:
                return 0
        return 0


        
                
            
                
            
