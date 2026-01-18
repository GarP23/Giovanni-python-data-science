#Listas
lista_de_algo = [29, True, "Giovanni", 3.14, "lo que hice si que mola"]
#podemos imprimir sus componentes

#print(lista_de_algo[4])
#print(lista_de_algo[1])
#print(lista_de_algo[0])
#print(lista_de_algo[3])

#Con indices negativos tambien se puede acceder a la lista, desde el final en adelante

print(lista_de_algo[-2])
print(lista_de_algo[2])
print(lista_de_algo[-1]) 


#Las lista tambien se puede modificar cada uno de sus elementos por otro elemento o incluso por otra lista
lista_interesante_nueva = ["musica", "arte", "poesia", 391, "familia", False, "amigos", 7.89]

print(lista_interesante_nueva)

lista_interesante_nueva[2] = "Física nuclear mola más como profesión"

print(lista_interesante_nueva)

lista_interesante_nueva[-3] = [675, 694, 00, "?"]

print(lista_interesante_nueva)

#se puede tambien seleccionar un grupo de elementos a travez de el uso de dos puntos y desde el valor inicial hasta el que queramos

print(lista_interesante_nueva[3:5])

#Tambien se puede jugar entre listas y a su vez agregar nuevos elementos a la lista utilizando el comando append

lista_distinta_juegos = [True, "jugar", 29, 3.14, "diversión", 29, 3.14]

lista_distinta_juegos.append("Agregar musíca a la vidaes como agregar un nuevo elemento a una lista")
print(lista_distinta_juegos)

lista_distinta_juegos.append(["rock", "clasica", "jazz", 404, False])
print(lista_distinta_juegos)

#tambien se puede contar cuantos elementos se repiten con el comando count

print(lista_distinta_juegos.count(29))

print(lista_distinta_juegos.count(3.14))

#realmente el metodo index funciona para encontrar la posicion de un elemento en la lista

print(lista_distinta_juegos.index("diversión"))

print(lista_distinta_juegos.index(True))

#De la misma froma a travez de otro comando como remove podemos remover un elemento de la lista

lista_distinta_juegos.remove(29)
print(lista_distinta_juegos)
lista_distinta_juegos.remove(3.14)
print(lista_distinta_juegos)
lista_distinta_juegos.remove(["rock", "clasica", "jazz", 404, False])
print(lista_distinta_juegos)   
lista_distinta_juegos.remove("Agregar musíca a la vidaes como agregar un nuevo elemento a una lista")
print(lista_distinta_juegos)


