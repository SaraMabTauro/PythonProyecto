def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero."

print("Selecciona una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingresa el número de la operación deseada: ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == '1':
    print("Resultado de la suma:", suma(num1, num2))
elif opcion == '2':
    print("Resultado de la resta:", resta(num1, num2))
elif opcion == '3':
    print("Resultado de la multiplicación:", multiplicacion(num1, num2))
elif opcion == '4':
    print("Resultado de la división:", division(num1, num2))
else:
    print("Opción no válida.")