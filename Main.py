from ManejaLibros import ManejaLibros


def op0():
    print("salir")

def op1():
    i=int(input("Ingrese el id de un libro \n"))
    l.muestra(i)

def op2():
    i=str(input("Ingrese una palabra \n"))
    l.busca(i)

switcher= {
    0:op0,
    1:op1,
    2:op2     
    }

def switch(op):
    func = switcher.get(op, lambda: print("Opción incorrecta"))
    func()

if __name__=='__main__':
    bandera=False
    l=ManejaLibros()
    l.Crear()
    while not bandera:
        print("---------------MENU-------------")
        print("1.Muestra segun id")
        print("2.Muestra segun palabra\n")

        op=int(input("Seleccione una opcion.\n"))
        switch(op)
        bandera=int(op)==0


