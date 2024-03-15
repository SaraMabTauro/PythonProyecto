#funcion para adquirir datos flotantes
def flt():
    n1 = float(input("inserte numero 1:"))
    n2 = float (input("inserte numero 2:"))

    return n1,n2


#funcion para adquirir cuatro datos string
def na():
    n1  =  input("Dame tu nombre (s):")
    ape =  input("Dame tu apellido (S):")
    

    return n1,ape



#Funcion para adquirir opcion de operacion matematica
def mat2():
    mat1 = input("Qué operacion quieres hacer? (suma/s,resta/r,multiplicacion/m,division/d,potencia)/p:")
    mat1.lower()

    return mat1


#Funcion para adquirir un dato string que puede usarse de manera general
def opt1():
    opt2=input("elige la operacion:")
    opt2.lower()

    return opt2


#funcion para Imprimir la presentacion de la app principal
def impr1():
    print ('este programa contiene diferentes opreaciones matematicas\n')
    print ('operaciones matematicas: mate\nOperaciones con caracteres: str\nEscribir en un archivo')

    return 0