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

# Con print podemos tener CADENAS FORMATEADAS o PLACEHOLDERS. Por ejemplo:
# Se usaba antiguamente asi, la funcion .format

print('{} esta {}'.format('Python', 'chido!!!'))

var1='Python'
var2='esta chulo'
# La nueva forma es con solo una F, y dentro de los placeholders van las variables a imprimir (texto solo no se puede)
# Tampoco funciona como antiguamente (poniendo las cadenas al final)
print(f'{var1} esta {var2}')