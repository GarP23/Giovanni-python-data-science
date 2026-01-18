#Aquí unos ejemlos de lo aprendido:

libros =["El diario de Nhoa", "Los hombres que no sabian amar a las mujeres", "El Zahir", "Relato de un Naufrago","Pideme lo que quieras"]
libros.append("Cien años de soledad")
print(libros)
libros.append("La quinta Ola")
print(libros)
libros.remove("Los hombres que no sabian amar a las mujeres")
print(libros)
libros.remove("Pideme lo que quieras")
print(libros)

Reaultado_final = libros[2:5]

#Tuplas

Resultado_final_tupla = (libros[2], libros[3], libros[4])
resultado = (Resultado_final_tupla.count("Relato de un Naufrago"), Resultado_final_tupla.index("Cien años de soledad"))
print(Resultado_final_tupla)
print(resultado)

#conjuntos
Capitulo_tres_leido = {libros[1], libros[3], libros[4]}
Capitulo_seis_leido = {libros[2], libros[4], libros[0]}
Capitulo_siete_leido = {libros[0], libros[2], libros[3], libros[1]}
print(Capitulo_tres_leido)
print(Capitulo_siete_leido)
resultado_capitulos_leidos = Capitulo_tres_leido.intersection(Capitulo_siete_leido)
print(resultado_capitulos_leidos)
resultado_capitulos_leidos_union = Capitulo_tres_leido.union(Capitulo_siete_leido)
print(resultado_capitulos_leidos_union)
resultado_capitulos_leidos_subset = Capitulo_tres_leido.issubset(Capitulo_seis_leido)
print(resultado_capitulos_leidos_subset)
resultado_capitulos_leidos = Capitulo_tres_leido & Capitulo_siete_leido
print(resultado_capitulos_leidos)