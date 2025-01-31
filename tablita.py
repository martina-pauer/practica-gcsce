#!/usr/bin/python3

# Obtiene tabla de un numero con bucle for y salto de valores (steping)

numero = int(input('Tabla del: '))

for producto in range(numero, (numero * 10) + 1, numero):
    # Desde el valor del producto unitario por steping en numero voy llegando al siguiente producto
    print('\n\t', numero, ' x ', producto // numero, ' = ', producto, '\n')
