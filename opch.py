# Modulos que contienen funciones a utilizar 
import opera
import fn

# Función para elegir qué tipo de operación matemática
def car5ss():
    resultado1 = 0  # condición inicial de variable resultado1
    s4r = fn.mat2()  # uso de función general para adquirir un dato string
    n1, n2 = fn.flt()  # función que adquiere dos datos flotantes

    # Realizar operación basada en el tipo adquirido
    match s4r:
        case 'suma':
            resultado1 = opera.sumar(n1, n2)  # operación sumar dentro del módulo
        case 'resta':
            resultado1 = opera.restar(n1, n2)  # operación restar dentro del módulo
        case 'multiplicacion':
            resultado1 = opera.multiplicar(n1, n2)  # operación multiplicar dentro del módulo
        case 'division':
            resultado1 = opera.dividir(n1, n2)  # operación dividir dentro del módulo
        case 'potencia':
            resultado1 = opera.potencia(n1, n2)  # operación potencia dentro del módulo
        case _:
            print("Hubo un error en el nombre de la operacion a realizar:")

    print(f"el resultado es: {resultado1} de la operacion: {s4r}")

# Llamar a la función principal
car5ss()
