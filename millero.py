#!/usr/bin/python3

'''
    Convierte millas a kilometros usando
    todo lo aprendido de variables hasta
    seccion 2, tema 13.
'''
# Obtengo medida en millas
distancia = float(input('Ingrese distancia en millas: '))
# Realizo conversion a la unidad de medida de distancia mayor, kilometros
conversion = distancia / 0.6213
'''
    Con concatenacion de coma (,) no
    es necesario casting de tipos para
    la función print. (lo seria en concatenacion de suma con "+")
'''
print(distancia, ' millas son ', round(conversion, 2), ' kilometros.')
