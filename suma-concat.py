#!/usr/bin/python3

'''
    Aplicar lo aprrendido hasta seccion 11 de cadenas
    de texto para diferenciar suma de numeros de
    concatenación de texto.
'''

numero_primero = 12

numero_segundo = 21

# Paso variables enteras a texto

cadena_primera = str(numero_primero)

cadena_segunda = str(numero_segundo)
# Muestro valores

print('\nValores: (' + cadena_primera + ', ' + cadena_segunda + ')\n')
texto = (cadena_primera + cadena_segunda)
# Muestro concatenación: 1221
print('\n\tConcatenacion: ' + texto + '.\n')

'''
    Muestro suma de pasar texto a enteros: 33.

    Forma legible y reutilizable aunque ligeramente
    mas lenta.
'''

resultado = int(numero_primero)

resultado = resultado + int(numero_segundo)
# resultado y texto son de tipos distintos, uno de texto y otro entero
# Muestra suma de enteros: 33 que es distinto de 1221
print('\n\tSuma: ' + str(resultado) + ', "' + str(resultado) + '" distinto de "' + texto + '": ' + str(resultado != int(texto)) + '.\n')
