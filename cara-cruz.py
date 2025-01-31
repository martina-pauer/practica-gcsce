#!/usr/bin/python3
import random
# Simula juego de lanzar moneda con cara o cruz

# Defino contadores de cada resultado

caras = 0

cruces = 0
# Simulo 10 lanzamientos
for lanza in range(10):
    # Toca una de las dos caras al azar
    cara = random.randint(1, 2)
    # Uso condiciones para obtener estadistica y traducir humanamente los numeros aleatorios
    if cara == 1:
        print('\tCara =)')
        # Cuento un resultado de 'cara'
        caras += 1
    else:
        print('\tCruz X')
        # Cuento un resultado de 'cruz'
        cruces += 1
# Digo cual gana o si empatan y por cuanto
if caras > cruces:
    print('\nCara con ', caras, ' veces.')
elif caras == cruces:
    print('\nHay empate con ', caras, ' veces.')
else:
    # Agote posibilidades de repeticiones de cara mayores o iguales a cruces: hay mas cruces
    print('\nCruz con ', cruces, ' veces.')
