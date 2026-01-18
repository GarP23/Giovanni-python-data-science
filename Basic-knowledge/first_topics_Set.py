#conjuntos

froma_de_cara = "ovalada"
tipo_de_cabello = "cafe oscuro"
color_de_ojos = "marrones"
manos = "gruesas y fuertes"

#un conjunto tienen elementos mutables, sin embargo no permite repetir elementos, no necesitan un orden y sus elementos no son accesibles por indice

primer_conjunto = {froma_de_cara, tipo_de_cabello, color_de_ojos, manos}
print(primer_conjunto)

# esto si que me interesa, resulta que un conjunto es
# representado con llaves, sin embargo como eso se utiliza dentro de un diccionario
# entonces lo que hacemos para poder definir conjuntos es utilizar la funcion set()
# y se podria hacer una combinacion de todos lo ya visto anteriormente, listas, tuplas y conjuntos

print("conjunto vacio")

set()

#para poder inicializarlo inicializarlo se puede dar una secuencai, como una lista o una tupla

set([29, True, "Giovanni", 3.14, "lo que hice si que mola"])
print(set([29, True, "Giovanni", 3.14, "lo que hice si que mola"])) 
set(("Los mejores fiolososofos son los que hablan de estoismo y lo practican", True, 3.14, 29, "Giovanni Ron Peralta", 3.14))
print(set(("Los mejores fiolososofos son los que hablan de estoismo y lo practican", True, 3.14, 29, "Giovanni Ron Peralta", 3.14)))


#como se puede observar uno de las funciones que se puede hacer con esto, es eliminar elementos repetidos dentro de una secuencia
#guardamos el conjunto en una variable -> conjunto_aprendiendo

conjunto_aprendiendo= set([29, True, "Giovanni", 3.14, "lo que hice si que mola", 29, 3.14, True])
print(conjunto_aprendiendo)

conjunto_aprendiendo.add("La vida es Bella")
print(conjunto_aprendiendo)


# Es posible operar entre conjuntos utilizando operadores matemáticos como la unión, intersección y diferencia.
print("Operaciones entre conjuntos")

ejemplo_conjunto_1 = set([5, 8, 9, 27, -3])
ejemplo_conjunto_2 = set([8, 9, 15, -3, 0, 42])
ejemplo_conjunto_3 = set([100, 200, 300])
ejemplo_conjunto_4 = set([-3, 5, 8, 9, 200, 15, 300, 42, 0])

print("Intersección")
print(ejemplo_conjunto_1, ejemplo_conjunto_2, ejemplo_conjunto_3, ejemplo_conjunto_4)
print(ejemplo_conjunto_1.intersection(ejemplo_conjunto_2))
print(ejemplo_conjunto_3.intersection(ejemplo_conjunto_4))

print("Unión")
print(ejemplo_conjunto_1.union(ejemplo_conjunto_4))
print(ejemplo_conjunto_3.union(ejemplo_conjunto_4))

#Se puede saber si un elemento esta o no incluido en otro conjunto con el conmando issubset

print(ejemplo_conjunto_3.issubset(ejemplo_conjunto_4))
print(ejemplo_conjunto_2.issubset(ejemplo_conjunto_4))
