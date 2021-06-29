# Ejercicio 5. Obtener la representacion inversa de una cadena de caracteres

#cadena = input('Ingresa la cadena: ')
#print(cadena[::-1])

# Lo logré sin ver el tutorial :3 <3

# De aquí pa' abajo el codigo del tutorial.

# Con un ciclo for iteraremos la cadena
cadena = 'Python'

# Con RANGE definimos que empiece desde el primer caracter (posicion 0)
# Y con LEN obtenemos la cantidad total de caracteres de la cadena, y poder obtener la ultima posicion
# Con el tercer argumento de RANGE podemos indicar en que orden hara el recorrido, osea -1

for i in range(len(cadena) -1, -1, -1):
# Finalmente imprimimos la POSICION actual de i en la cadena:
# Agregamos el end para que muestre el resultado del ciclo en una sola linea y no asi:
#   n
#   o   
#   h
# etc.
    print(cadena[i], end='')

print()
print(cadena[::-1])