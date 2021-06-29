# Ejercicio 3. Obtener la fecha y hora actuales del sistema.

# Lo primero que tenemos que hacer es importar la libreria datetime, que nos permite trabajar con horas y fechas:
import datetime
# Ahora, de la funcion DATETIME, invocaremos la funcion NOW

hora_actual = datetime.datetime.now()
print(hora_actual)

# Vamos a formatear sobre el objeto datetime, por que muestra la fecha asi: 2021-06-28 19:40:05.941767

# Para formatear horas y fechas, tenemos la funcion STRFTIME
# ver https://strftime.org/ para saber como formatear

print(hora_actual.strftime('%A %d %B %Y - %I:%M:%S %p'))
# Podemos formatear de distintas maneras, depende como queramos o necesitemos.
print(hora_actual.strftime('%d/%m/%Y %H:%M:%S %p'))