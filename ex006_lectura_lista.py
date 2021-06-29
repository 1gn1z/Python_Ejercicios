# Ejercicio 6. Obtener un conjunto de números separados por comas y crear una lista

# 2, 8, 9, 0, 1, 8

conjunto = input('Escriba varios números separados por comas: ')

# Como sabemos, la funcion input devuelve una CADENA, asi que hay que transformar esa cadena en una lista.
# el metodo SPLIT hace exactamente eso, convertir una CADENA en una LISTA, justo lo que necesitamos ;)

# A nuestra cadena debemos pasarle el metodo SPLIT, indicando que separador queremos usar, ejemplo:

# >>> 1, 2, 3.split(',')

# Como ya tenemos la variable, usaremos otra variable para indicar que la variable conjunto use el método split:

lista = conjunto.split(',')
print(type(lista))
print(lista)

# IMPORTANTE Los elementos que retorna split son CADENAS.
# ['2', ' 8', ' 1', ' 4']

# IMPORTANTE Vemos que todos los numeros excepto el 2 tienen un espacio antes del número, esto pasa debido a que split transforma la cadena
# tal cual fue ingresada: 2, 8, 1, 4. Como vemos, hay un espacio antes del 8 el 1 y el 4, por eso en el resultado que arroja Python
# los imprime con un espacio. 

