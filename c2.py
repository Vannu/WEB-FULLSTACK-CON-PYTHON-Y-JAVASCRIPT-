
###

#1. Escribe un programa que acepte el radio de un circulo del usuario y calcule el area.
#2. Escribe un programa que acepte un numero entero (n) y calcule el valor de n+nn+nnn
#3. Escribe un programa que acepte una cadena de caracteres y cuente el tamaño de la cadena y cuantas veces aparece la letra A (mayuscula y minuscula)
#4. Escribe un programa que muestre la hora actual con una suma de dos horas adicionales

###

# 1:

radioCirculo = float(input("Ingrese radio: \n"))
pi = float(3.14)
area = pi * radioCirculo ** 2
print(area)

#  2:

n = int(input('Ingrese un numero entero: \n'))
suma = n + n*2 + n*3
print(suma)

# 3:
cadena = input("Ingrese un texto: ")
total_caracteres = len(cadena)
print ("Total de caracteres: ", total_caracteres)
cont = cadena.count("a")
print("Cantidad de letas con (a) en la cadena es de: ",cont)

# 4:

import datetime as d

horaActual = d.datetime.now()
print('Hora actual: ',horaActual,'\n')
horaSuma = horaActual + d.timedelta(hours= 2)
print('Hora despues de dos horas: ',horaSuma)
