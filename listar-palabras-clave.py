#!/usr/bin/python3

'''
    Practica de seccion 7 curso de Narges Berry en udemy de listar
    palabras reservadas de Python por Martina Pauer
'''

import keyword

# Crea archivo con todas las palabras reservadas de python
archivo = open('python-keywords.txt', 'w')
# Crea un contador de palabras reservadas
palabra = 1
# Por cada palabra de la lista de palabras clave (keywords), agrego al archivo
for palabra_clave in keyword.kwlist:
    '''
        Agrego una palabra y sigo contando una palabra mas.

        El archivo sigue sintaxis: <numero-de-palabra>. <palabra_clave>
    '''
    archivo.write('%s. %s\n' % (palabra, palabra_clave))
    # Al terminar dara una palabra mas porque en todo el bucle cuenta otra
    palabra += 1
'''
    Para solucionar conteo extra de palabras, al
    finalizar la iteracion resto en uno a la varible
'''
palabra -= 1
# Muestro cuantas palabras clave se encontraron
print('%s palabras claves encontradas guardadas en "python-keywords.txt".\n' % palabra)
# Elimino varible de memoria
del palabra
# Cierro el archivo para liberarlo al sistema
archivo.close()
