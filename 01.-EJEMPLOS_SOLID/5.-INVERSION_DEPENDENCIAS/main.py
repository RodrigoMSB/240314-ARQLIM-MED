from EmpleadoNormal import EmpleadoNormal
from Asistente import Asistente
from EmpleadoAdministrativo import EmpleadoAdministrativo
from GestorEmpleados import GestorEmpleados

# Crear instancias de empleados
empleado_normal = EmpleadoNormal("Rodrigo")
asistente = Asistente("María")
empleado_administrativo = EmpleadoAdministrativo("Pedro")

# Crear instancia de GestorEmpleados
gestor_empleados = GestorEmpleados()

# Contratar empleados
gestor_empleados.contratar_empleado(empleado_normal)
gestor_empleados.contratar_empleado(asistente)
gestor_empleados.contratar_empleado(empleado_administrativo)

# Mostrar lista de empleados
print("\nLista de empleados:")
for empleado in gestor_empleados.empleados:
    print(f"- {empleado.nombre}")

# Despedir un empleado
gestor_empleados.despedir_empleado(empleado_normal)

# Mostrar lista de empleados actualizada
print("\nLista de empleados actualizada:")
for empleado in gestor_empleados.empleados:
    print(f"- {empleado.nombre}")

