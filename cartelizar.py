#!/usr/bin/python3

'''
    Muestra en vertical en parentesis si no es espacio en blanco
    el nombre de una ciudad (sirve de boceto para los carteles)
'''
# Obtengo nombre de ciudad
ciudad = input('Ingrese nombre de ciudad: ')
# Mientras no haya al menos 4 caracteres solicito de nuevo el nombre
while len(ciudad) < 4:
    ciudad = input('\n\tIngrese nombre de 4 caracteres como minimo: ')
# Comienzo a mostrar
print('\n')
# Recorro cada uno de los caracteres del nombre
for caracter in ciudad:
    if (caracter != ' ') and (caracter != ''):
    # Muestro si no es caracter nulo o en blanco
        print('\t(', caracter, ')\t')
    else:
        # Nueva linea cuando no hay letras que mostrar
        print('\n')
# Termino de mostrar
print('\n')
