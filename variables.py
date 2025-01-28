#!/usr/bin/python3

# Obtiene 3 valores y calcula promedio usando asignacion en cadena
primera_variable, segunda_variable, tercera_variable = int(input('\n\tIngrese valor 1: ')), int(input('\n\tIngrese valor 2: ')), int(input('\n\tIngrese valor 3: '))
# Promedio entero entre los tres valores
resultado = ((primera_variable + segunda_variable + tercera_variable) // 3)
# Muestro resultado
print('\nPromedio entre los valores "%i", "%i" "%i" es: %i.\n' % (primera_variable, segunda_variable, tercera_variable, resultado))
