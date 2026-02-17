#Cree un función en python llamada calculadora, la cual debe tomar los parámetros (num_1, num_2, operacion)
#Debe ser capaz de realizar toda la lógica de un calculadora simple como: sumar, restar, multiplicar y dividir.
#Nota: Las entradas serán proporcionadas por el usuario.
#Pista: Este código es un ejemplo de una suma 



print("========Calculadora==========")
operacion = input("¿Que operacion quieres realizar +, -, *, /? ")
num_1 = int(input("Escribe el primer numero: "))
num_2 = int(input("Escribe el segundo numero: "))

def suma(num_1, num_2):
    return num_1 + num_2

if operacion == "+":
    resultado = suma(num_1, num_2)
    print("El resultado de la suma es: ", resultado)

def resta(num_1, num_2):
    return num_1 - num_2

if operacion == "-":
    resultado = resta(num_1, num_2)
    print("El resultado de la resta es: ", resultado)

def multiplicacion(num_1, num_2):
    return num_1 * num_2

if operacion == "*":
    resultado = multiplicacion(num_1, num_2)
    print("El resultado de la multiplicacion es: ", resultado)

def division(num_1, num_2):
    return num_1 / num_2

if operacion == "/":
    resultado = division(num_1, num_2)
    print("El resultado de la division es: ", resultado)