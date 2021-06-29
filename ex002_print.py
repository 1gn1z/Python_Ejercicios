# Ejercicio 2. Exponer el uso básico de la función print.

# El texto (dentro de los parentesis) es el ARGUMENTO de la FUNCION print :D
#print('Ejemplo básico de uso de la función print')


# Con el argumento "end" especificamos con que caracter vamos a terminar la impresión del texto.
# En este caso, vemos que al poner el salto de linea, al imprimirlo termina la impresion con un salto de linea.
print('Ejemplo básico de uso de la función print 2', end='\n')

print()
# Al imprimir asi, se muestra correctamente el texto.
print('Python', 'esta', 'chido!')

# Vamos a usar el argumento SEP (separator), para indicar que caracter usaremos como separador
print('Python', 'esta', 'chido!', sep='-')
# Puede ser cualquier caracter que queramos usar (o necesitemos) como separador:
print('Python', 'esta', 'chido!', sep='*')
# Puede ser mas de un caracter :D
print('Python', 'esta', 'chido!', sep='--------')
print('Python', 'esta', 'chido!', sep=':')

