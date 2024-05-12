from EmpleadoNormal import EmpleadoNormal
from Asistente import Asistente
from EmpleadoAdministrativo import EmpleadoAdministrativo

# Crear instancias de diferentes empleados
empleado_normal = EmpleadoNormal()
asistente = Asistente()
empleado_administrativo = EmpleadoAdministrativo()

# Probar los métodos de los empleados
print("Empleado normal:")
empleado_normal.trabajar_documentos()

print("\nAsistente:")
asistente.trabajar_documentos()
asistente.asistir_reuniones()

print("\nEmpleado administrativo:")
empleado_administrativo.trabajar_documentos()
empleado_administrativo.asistir_reuniones()
empleado_administrativo.realizar_tareas_administrativas()
