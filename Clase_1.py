# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Variables

a = 3
print(type(a))
a = "hola"
print(type(a))
a = 3.5
print(type(a))
a = True
print(type(a))

print ('Hola Mundo')
print ('Hola Mundo dos')

print ("I can't do it")
print ('His name is Roberto')

# Operaciones

# Suma

a = 5
b = 2
c = a + b
print(c)

# Resta

a = 5
b = 2
c = a - b
print(c)

# Multiplicacion

a = 5
b = 2
c = a * b
print(c)

# Division

a = 5
b = 2
c = a / b
print(c)

# Division parte entera

a = 5
b = 2
c = a/b
print(c)

# Potencia
a = 2
c = a **6

# Raiz cuadrada

a = 16
b = a ** (1/2)

import math
raiz = math.sqrt(a)
print(raiz)

# Tipos de datos

# String str

a = "Hola Mundo"
a = 'Hola Mundo'

#Entero int
a = 5

# Decimal float
a = 5.6

# Booleano bool
x = True
y = False

# Conversiones entre tipos de datos

# Convertir de x a entero

a = '3'
b = int(a)
print(type(b))

# Convertir de x a String

a = 3
b = str(a)
print(type(b))

# Concatenaciones

a = 'hola'
b = 'mundo'
c = a + ' ' + b

a = 'hola'
b = a * 5
print(b)


# Capturar por pantalla

nombre = input('Digite su nombre')
print('Hola', nombre)

nombre = input('Digite su nombre')
print('Hola', nombre, sep='**', end='FIN')

nombre = input('Digite su nombre')
print('Hola' + nombre)

# Interpolacion

nombre = input('Digite su nombre')
print(f' Su nombre es {nombre}')

# Ejercicios

# Ejercicio 1
n1 = int(input('Digite el primer numero'))
n2 = int(input('Digite el segundo numero'))
suma = n1 + n2
print(f'La suma de {n1} + {n2} es: {suma}')

# Ejercicio 2
n1 = int(input('Digite el primer numero'))
cuadrado = n1 ** 2
print(f'El numero {n1} al cuadrado es : {cuadrado}')

# Ejercicio 3

valor = int(input('Ingrese el valor del producto'))
producto = valor * 0.80
ahorrado = valor - producto

print(f'El valor inicial del producto es: ${valor:,} ')
print(f'El valor del producto con descuento es: ${producto:,}')
print(f'El valor ahorrado es: ${ahorrado:,}')








