# Ejercicio 4: Solicitar el valor del radio de un círculo para calcular su área.

# Vamo' a importar la libreria MATH, especificamente lo que necesitamos, la parte del PI:
from math import pi

radio = int(input('Ingrese el radio del círculo: '))

# Bucamos la formula en internet:
#El área de un círculo es pi multiplicado por el radio al cuadrado (A = π r²).

area = pi * radio**2
print(f'El área del círculo es: {area}')

# TODO ESTO LO HICE SIN VER EL TUTORIAL Y YA QUEDÓ :31