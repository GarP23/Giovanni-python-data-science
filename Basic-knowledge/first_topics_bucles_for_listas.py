from ast import For


ventas = [120, 150, 90, 200]

for v in ventas:
    print(v)


total = 0

for v in ventas:
    total = total + v

print(total)


Productos = ["camisa", "esmeralda", "zapatos", "hipopotamo", "compostela ", "ola", "mar", "sol", "luna"]

for p in Productos:
    cantidad_de_letras = len(p)
    print(f"El producto {p} tiene {cantidad_de_letras} letras")

#Ahora para ir complicandolo un poco más vamos a sumar la cantidad de letras de todos los productos así
suma_letras = 0

for p in Productos:
    cantidad_de_letras = len(p)
    suma_letras = suma_letras + cantidad_de_letras  
print(f"La suma total de letras de todos los productos es: {suma_letras}")

#porque va la f antes de las comillas? Porque es una cadena formateada, es decir que dentro de las llaves podemos poner variables y se van a evaluar e imprimir su valor en lugar de la variable en sí.
#Ahora un ejemplo un poco más complejo, vamos a sumar solo las letras de los productos que tienen más de 5 letras

suma_letras_mayores_a_5 = 0

for p in Productos:
    cantidad_de_letras = len(p)
    if cantidad_de_letras < 3:
        suma_letras_mayores_a_5 = suma_letras_mayores_a_5 + cantidad_de_letras

print(f"La suma total de letras de los productos con más de 5 letras es: {suma_letras_mayores_a_5}")

#Ahora un ejemplo mucho mas coplejo, vamos a elegir una letra especifica y vamos a cer cuantas veces se repite en cada uo de los productos
letra_elegida = input("Ingresa una letra para buscar en los productos: ")
suma_letras_elegidas = 0   
for p in Productos:
    for letra in p:
        if letra == letra_elegida:
            suma_letras_elegidas = suma_letras_elegidas + 1
print(f"La letra {letra_elegida} se repite {suma_letras_elegidas} veces en cada palabra de la lista de productos.")

#ahora vamos a hacer un ejemplo donde tenemos una lista de numeros y queremos sumar solo los numeros pares
numeros_random = [3, 4, 7, 8, 10, 13, 16, 19, 22, 25]

suma_de_números_pares = 0

for s in numeros_random:
    if s % 2 == 0:
        suma_de_números_pares = suma_de_números_pares + s
print(f"La suma de los números pares en la lista es: {suma_de_números_pares}")
print(f"la lista de numeros es: {numeros_random}")
#utilizando el end tendiramos:
print("Los números pares en la lista son: ", end="")
for s in numeros_random:
    if s % 2 == 0:
        print(s, end=" ")
#vamos a responder una pregunta
#por que si se utiliza el print antes de el ultimo for
#se imprime toda la lista de numeros enuna sola linea 
#y si se utiliza el print dentro del for
#se imprime cada numero en una linea diferente? pues eso se debe a que cuando se utiliza el print dentro del for
#se esta imprimiendo cada numero en cada iteracion del for y cuando se utiliza el print fuera del for
#se esta imprimiendo la lista completa de numeros en una sola linea.
for s in numeros_random:
    if s % 2 != 0:
        print(f"los números ahora son {s}")

#Ahora vamos con ejercios más chungos para aprender a recorrer listas con enunciados y todo paso a paso,
#por ejemplo:
#Dada una lista de calificaciones de estudiantes, calcular el promedio de las calificaciones aprobadas (mayores o iguales a 60).
calificaciones = [55, 70, 85, 40, 90, 60, 75, 30, 95]
suma_de_calificaciones = 0
alumnos_aprovados = 0
for c in calificaciones:
    if c >= 60:
        suma_de_calificaciones = suma_de_calificaciones + c
        alumnos_aprovados = alumnos_aprovados + 1
promedio = suma_de_calificaciones / alumnos_aprovados
print(f"El promedio de las calificaciones aprobadas es: {promedio}")    

#Dada una lista de edades, contar cuántas personas son mayores de edad (18 años o más).
edades = [15, 22, 17, 30, 45, 12, 18, 25, 16]
mayores_de_edad = 0
menores_de_edad = 0
for  e in edades:
    if e >= 18:
        mayores_de_edad = mayores_de_edad + 1 
    elif e < 18:
            menores_de_edad = menores_de_edad + 1
    else:
            print("Error en la edad")
print(f"el numero de personas mayores de edad es: {mayores_de_edad}")
print(f"el numero de personas menores de edad es: {menores_de_edad}")

#Dada una lista de palabras, crear una nueva lista que contenga solo las palabras que tienen más de 4 letras.
palabras = ["sol", "luna", "estrella", "cielo", "mar", "montaña", "río", "bosque"]
palabras_mayores_a_4 = []
palabras_menores_a_4 = []
for p in palabras:
    if len(p) < 5:
        palabras_menores_a_4.append(p)
    else:
        palabras_mayores_a_4.append(p)
        #aqui el append funciona como.....???
print(f"La lista de palabras con más de 4 letras es: {palabras_mayores_a_4}")
print(f"La lista de palabras con menos de 4 letras es: {palabras_menores_a_4}")

#ahora te explico por que en este caso append si funciona para agregar elementos a la lista
#porque en este caso estamos trabajando con listas y las listas son mutables como puedes ver en el archivo proyecto_1.1.py
#por lo tanto podemos agregar elementos a la lista utilizando el metodo append, ejemplo:
palabras_mayores_a_4.append("nube")
print(f"La lista de palabras con más de 4 letras es: {palabras_mayores_a_4}")


