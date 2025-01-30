#!/usr/bin/python3

'''
    Dice en centimetros a partir de las pulgadas, la resolución de una pantalla.
'''

# Obtiene cuantas pulgadas es la diagonal que une dos esquinas de la pantalla
pulgadas_diagonal = float(input('\tIngrese cuantas pulgadas(in) tiene la pantalla: '))

PI = 3.14

EULER = 2.71

'''

    Uso trigonometria para obtener ancho y alto:


        - La altura es opuesta a la diagonal, cateto opuesto
          sobre la hipotenusa diagonal a 45 radianes, usa
          seno(0.85)

        - La aunchura es adyacente(es el piso) de la diagonal,
          cateto adyacente sobre esa hipotenusa usa coseno
          de 45 radianes(0.52).
'''
# Uso valor precalculado para ahorrar algo de poder de comput, energia y tiempo
altura = 0.85

anchura = 0.52

# Multiplico por la diagonal obtenida a ambas variables, no usar asignacion en cadena para evitar errores
altura *= pulgadas_diagonal

anchura *= pulgadas_diagonal
# Paso a centimetros(estan en pulgadas que cada una es 2.54 cm)
altura = (altura * 2.54)

anchura = (anchura * 2.54)
# Corrijo error agregando PI diferente en 1 a la superficie vertical
altura += (PI - 1)
# Corrijo error agregando perdida de medio EULER a la superficie horizontal
anchura -= (0.5 * EULER)
# Redondeo resultados para que se vean mejor, no necesito decimales de precision

altura = round(altura)

anchura = round(anchura)
# Digo si hay mucha o iguak altura y digo el resultado
print('\n- ¿La altura es mayor al ancho?\n\t- ', altura > anchura, '\n')

print('- ¿La altura y el ancho son iguales?\n\t- ', altura == anchura, '\n')

print('\n\tLa pantalla es de ', anchura, 'cm de ancho por ', altura, 'cm de alto, casi ', (anchura * altura), 'cm cuadrados.\n')
# Paso a metros

altura /= 100

anchura /= 100
# Necesito enteros

anchura = round(anchura)

altura = round(altura)
# Muestro
print('\n\tLa pantalla es de ', anchura, ' metros de ancho por ', altura, ' metros de alto, casi ', (anchura * altura), ' metros cuadrados.\n')
# Paso a pulgadas

altura *= (100 // 2.54)

anchura *= (100 // 2.54)

print('\n\tLa pantalla es de ', anchura, 'in de ancho por ', altura, 'in de alto, casi ', (anchura * altura), 'in cuadradas.\n')
