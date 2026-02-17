# Loops

mi_lista = [1,2,3,4,5]

for i in mi_lista: 
    print ("El numero es:", i)

resultado = 0
for i in mi_lista:
    resultado += i

print(f"El resultado de la suma de mi lista es: {resultado}")

for i in range (2, 8):
    print (i)

mi_lista_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]

for i in mi_lista_2:
    if i !="lunes":
       print (f"Feliz {i}!")



#Dada la lista my_list_2 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
#Imprime cada elemento de la lista 3 veces y cuando sea lunes no la incluyas.
#Pista: usa los tipos de loops while y for en el mismo programa para lograrlo
#Resultado:
#Martes
#Miercoles
#Jueves
#Viernes
#Martes
#Miercoles
#Jueves
#Viernes
#Martes
#Miercoles
#Jueves
#Viernes

mi_lista_2 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

for lista in mi_lista_2:
    if lista == "Lunes":
        continue

    i = 0

    while i < 3:
        print(lista)
        i += 1
