#Modulo para adquirir string
import fn

#funcion que contatena dos datos string
def concat():
    a,b = fn.na() #adquiere datos string
    vacar1  =  input ("¿cual es tu carrera?:")
    cuatr1  =  input ("¿Cual es tu cuatrimestre?:")
    c = a + ' '+ b + ' ' + vacar1 +' ' + cuatr1 #concatena los datos
    
    print (c)

    return 0

concat()
