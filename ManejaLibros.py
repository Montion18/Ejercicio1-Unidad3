from Capitulos import capitulos
from Libro import libro
import csv
class ManejaLibros:
    __lista=[]

    def Crear(self):
        archivo=open("libros.csv")
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            if len(fila)==6:
                l=libro(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]),int(fila[5]))
                self.__lista.append(l)
            else:
                if len(fila)==2:
                    cap=capitulos(fila[0],fila[1])
                    l.setcapitulo(cap)
                    
    def muestra(self,id):
        for i in range(len(self.__lista)):

            if self.__lista[i].getid() == id:
                print("titulo:",self.__lista[i].gettit())
                
                self.__lista[i].getnombcap()
                print("\nCantidad total de paginas: ",self.__lista[i].gettotalpag())
                return
            
        return print("id incorrecto")   
    def busca(self,palabra):
        for i in range(len(self.__lista)):
            if self.__lista[i].gettit().find(palabra)>=0 or self.__lista[i].buscacapitulos(palabra)>0:
                 print("Libro: ",i+1)
                 print("titulo:",self.__lista[i].gettit())
                 print("Autor",self.__lista[i].getaut())
                 
            else:
                print("No se encontro esa palabra en el libro ",i+1)
                  
                        
                    
               
            

            

            
        

