from EmpleadoTiempoCompleto import EmpleadoTiempoCompleto
from EmpleadoTiempoParcial import EmpleadoTiempoParcial

def calcular_salarios(empleados):
    """
    Función para calcular los salarios de una lista de empleados.

    Args:
        empleados (list): Lista de objetos de tipo Empleado.

    Returns:
        dict: Un diccionario que mapea el nombre de cada empleado con su salario.
    """
    salarios = {}
    for empleado in empleados:
        salario = empleado.calcular_salario()
        salarios[empleado.nombre] = salario
    return salarios


# Creamos instancias de diferentes tipos de empleados
empleado1 = EmpleadoTiempoCompleto("Juan", salario_mensual=3000)
empleado2 = EmpleadoTiempoParcial("Pedro", horas_trabajadas=80, salario_hora=20)

# Calculamos los salarios de los empleados y los mostramos
salarios = calcular_salarios([empleado1, empleado2])
for nombre, salario in salarios.items():
    print(f"{nombre}: ${salario}")
