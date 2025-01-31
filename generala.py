#!/usr/bin/python3

'''
    Usa lo aprendido de operadores lógicos y
    números aleatorios para un juego de dados:

        Juego de dados General (reglas):

            -   Hay 5 dados de 6 caras con numeros del 1 al 6

            -   Por cada turno se puede tirar hasta 3 veces el dado

            -   Deben ocurrir alguna de estas coincidencias:

                    Generala: todos los dados iguales

                    Full: tres dados iguales distintos a otros dos dados iguales

                    Poker: Cuatro iguales y uno desigual

                    Escalera: Del menor al mayor numero de los dados hay una distancia de 1 entre cada dado
'''
# Importo modulo para agregar azar
import random
# Defino cuantos tiros habra y valor de primer tiro
tiros_restantes = 3
# Hago primer tiro reduciendo en 1 los tiros restantes
print('\n\tPRIMER TIRO\n')
tiros_restantes -= 1
# Deben ser 5 dados con valores del 1 al 6
dado_1 = random.randint(1, 6)

dado_2 = random.randint(1, 6)

dado_3 = random.randint(1, 6)

dado_4 = random.randint(1, 6)

dado_5 = random.randint(1, 6)
# Muestro resultado de primer tiro y pregunto con 'si' o 'no' para tirar otra vez si hay 1 tiro o mas disponibles
print('\nLos dados dieron: [', dado_1, '] [', dado_2, '] [', dado_3, '] [', dado_4, '] [', dado_5, ']\n')

continuar = input('¿Desea continuar? si o no: ')
# Continuo segun las desiciones del usuario
if continuar == 'si':
    print('\n\tSEGUNDO TIRO\n')
    tiros_restantes -= 1
    # Deben ser 5 dados con valores del 1 al 6
    dado_1 = random.randint(1, 6)

    dado_2 = random.randint(1, 6)

    dado_3 = random.randint(1, 6)

    dado_4 = random.randint(1, 6)

    dado_5 = random.randint(1, 6)
    # Muestro resultado de primer tiro y pregunto con 'si' o 'no' para tirar otra vez si hay 1 tiro o mas disponibles
    print('\nLos dados dieron: [', dado_1, '] [', dado_2, '] [', dado_3, '] [', dado_4, '] [', dado_5, ']\n')

    tercera = input('¿Desea continuar? si o no: ')

    if tercera == 'si':
        print('\n\tTERCER TIRO\n')
        tiros_restantes-= 1
        # Deben ser 5 dados con valores del 1 al 6
        dado_1 = random.randint(1, 6)

        dado_2 = random.randint(1, 6)

        dado_3 = random.randint(1, 6)

        dado_4 = random.randint(1, 6)

        dado_5 = random.randint(1, 6)

        # Muestro resultado de último tiro
        print('\nLos dados dieron: [', dado_1, '] [', dado_2, '] [', dado_3, '] [', dado_4, '] [', dado_5, ']\n')
# Una vez obtenidos con que quinteto de dados se quedo la persona, digo que tipo de coincidencia es
if (dado_1 == dado_2) and (dado_2 == dado_3) and (dado_3 == dado_4) and (dado_4 == dado_5):
    print('\n[GENERALA: todos iguales]\n')
else:
    # Algunas condiciones son complejas y debo expresarlas de a poco para que sean legibles
    # dados 12 o 13 iguales
    condiciones_full = (dado_1 == dado_2) or (dado_1 == dado_3)
    # dados 14 o 15 iguales
    condiciones_full = condiciones_full or (dado_1 == dado_4) or (dado_1 == dado_5)
    # Primer dado eliminado, sigo con los otros 4 en busca de dos iguales
    # dados 23 y/o 24 iguales
    condiciones_full = condiciones_full or (dado_2 == dado_3) or (dado_2 == dado_4)
    # Dados 25 y/o 34 iguales
    condiciones_full = condiciones_full or (dado_2 == dado_5) or (dado_3 == dado_4)
    # Ya habre visto en este punto si habia dados iguales (no puedo asegurar si son 2, 3 o 4 aunque ya descarte que 5 lo sean en el otro condicional)
    condiciones_full = condiciones_full or (dado_3 == dado_5) or (dado_4 == dado_5)
    # Se que hay al menos dos iguales, veo si hay 3
    condiciones_full = condiciones_full and (dado_1 == dado_2) and (dado_2 == dado_3)
    # Veo otras posibilidades si no son los primeros 3 iguales: 124, 134, 234, 324, 432, 423, 431, 413, 421, 412
    # 124
    condiciones_full = condiciones_full or (dado_1 == dado_2) and (dado_2 == dado_4)
    # 134
    condiciones_full = condiciones_full or (dado_1 == dado_3) and (dado_3 == dado_4)
    # 234
    condiciones_full = condiciones_full or (dado_2 == dado_3) and (dado_3 == dado_4)
    # 324
    condiciones_full = condiciones_full or (dado_3 == dado_2) and (dado_2 == dado_4)
    # 432
    condiciones_full = condiciones_full or (dado_4 == dado_3) and (dado_3 == dado_2)
    # 423
    condiciones_full = condiciones_full or (dado_4 == dado_2) and (dado_2 == dado_3)
    # 413
    condiciones_full = condiciones_full or (dado_4 == dado_3) and (dado_3 == dado_1)
    # 421
    condiciones_full = condiciones_full or (dado_4 == dado_2) and (dado_2 == dado_1)
    # 412: No hago mas porque es muy engorroso, cubre varios casos y sirve para entender el concepto
    condiciones_full = condiciones_full or (dado_4 == dado_1) and (dado_1 == dado_2)

    # Manejo así otros casos solo por razones de legibilidad para evitar sobre anidamiento aunque hace al script mas lento 
    if (condiciones_full):
        print('\n[FULL: dos iguales distintos a otro grupo de tres iguales]\n')
# HASTA ACA DEJO SINO ES MUY ENGORROSO LA CANTIDAD DE CONDICIONES Y ES SOLO PARA PRACTICAR, TODO ESTO ME TOMO 2 HORAS
