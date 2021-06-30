# Ejercicio 9. Mostrar la fecha de un evento almacenada en una tupla.

fecha_evento = (2023, 9, 14)    # objeto tupla.

# Podemos mostrar la fecha tal cual, con un mensaje:

print('El evento programado será para la fecha:', fecha_evento)

# Pero sigue mostrandolo tal cual. Vamo a usar unos PLACEHOLDERS:

# Estos PLACEHOLDERS se mapean a cada uno de los elementos que tiene la tupla
print('El evento programado será para la fecha: %i %i %i' % fecha_evento)    # %i es de INTEGER o entero. En lugar de coma ponemos %


