#Librerias del desarrollador
import fn
import opch
import concat1
import opera

#Librerias del sistema operativo
import os
from time import sleep

#limpia pantalla
os.system("cls")

#valor inicial de la variable para la condicion del while
opc1 = 's'


#ciclo principal
while(opc1=='s'):
    #imprime presentacion funcion impr1 dentro del modulo fn
    fn.impr1()
    #adquiere la opcion del usuario, usa la funcion opt1 dentro del modulo fn
    opt = fn.opt1()


    #case para elegir el modulo de operaciones o de concatenacion
    match opt:
        case 'operacion matematica':
            opch.car5ss() #Modulo de operaciones matematicas
        case 'str':
            concat1.concat() #Modulo de concatenacion
        case _:
            print ('Error al escribir la opcion...')
            
    print ('Desea continuar con el programa? (Si/No)') # seguir con el programa
    opc1 = fn.opt1() #Funcion que adquiere un dato string
    opc1 = opc1.lower()
    os.system('cls') #Limpia la pantalla
    sleep (15) #Espera 15 segundos 
print ('Gracias por usar nuestra APP, bye bye :) ')
sleep (10) #Espera 10 segundos
os.system("cls")
