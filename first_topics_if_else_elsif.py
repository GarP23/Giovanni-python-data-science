numero = int(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo")
else:
    print("El número es negativo")

Temperarura = float(input("Ingresa la temperatura fuera de casa en grados Celsius: "))  

if Temperarura < 125 and Temperarura >= 25:
    print("Esta muy agradable afuera")
elif Temperarura > 125:
    print("Es un horno afuera")
else:
    print("La temperatura es baja afuera")

Servicio_internet = bool(int(input("¿Tienes servicio de internet? (1 para sí, 0 para no): ")))  

if Servicio_internet==True:
    print("Puedes jugar fornite")
else:
    print("No puedes jugar fornite")    

Horario_diario = int(input("Ingrese una hora: "))

if Horario_diario >= 6 and Horario_diario < 12:
    print("Es hora de ir a el trabajo")
elif Horario_diario >= 12 and Horario_diario < 18:
    print("Es momento de comida repaso y actividad de ocio")
else:
    print("Es hora de descansar y de dormir")