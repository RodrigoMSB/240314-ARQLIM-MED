from ManejadorDatos import ManejadorDatos
from MySQL import MySQL
from MongoDB import MongoDB

# Instanciamos un objeto de cada clase
manejador = ManejadorDatos()
mysql = MySQL()
mongodb = MongoDB()

# Probamos el método procesar de ManejadorDatos con cada objeto
print("Procesando MySQL:")
manejador.procesar(mysql)

print("\nProcesando MongoDB:")
manejador.procesar(mongodb)
