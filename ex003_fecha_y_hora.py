# Ejercicio 3. Obtener la fecha y hora actuales del sistema.

# Lo primero que tenemos que hacer es importar la libreria datetime, que nos permite trabajar con horas y fechas:
import datetime
# Ahora, de la funcion DATETIME, invocaremos la funcion NOW

hora_actual = datetime.datetime.now()
print(hora_actual)

# Vamos a formatear sobre el objeto datetime, por que muestra la fecha asi: 