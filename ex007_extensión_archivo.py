# Ejercicio 7: Obtener la extensión de un archivo especificado por el usuario.

nombre_archivo = input('Ingrese el nombre del archivo: ')

# Al igual que en el ejercicio 6, usaremos el metodo SPLIT, que nos permite especificar que caracter usaremos como separador.

# main.py

# Tenemos el nombre del archivo y su extension (despues del punto)
# Sobre otra variable, vamos a guardar el resultado de invocar el metodo split, y le indicamos que el separador
# va a ser el punto.

partes_nombre_archivo = nombre_archivo.split('.')
print(partes_nombre_archivo)

# Podemos usar slicing para obtener solo el segundo elemento de la cadena:
# Sin ver el tuto esto :3 <3
print(partes_nombre_archivo[1])
