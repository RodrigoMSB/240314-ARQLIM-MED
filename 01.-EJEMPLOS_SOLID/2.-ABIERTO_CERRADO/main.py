from EmpleadoNormal import EmpleadoNormal
from Asistente import Asistente
from CalculadoraSalario import CalculadoraSalario

# Crear instancias de empleados
empleado_normal = EmpleadoNormal("Juan", 1500.0)
asistente = Asistente("María", 2000.0)

# Crear instancia de CalculadoraSalario
calculadora_salario = CalculadoraSalario()

# Calcular salario de los empleados
salario_empleado_normal = calculadora_salario.calcular_salario(empleado_normal)
salario_asistente = calculadora_salario.calcular_salario(asistente)

# Mostrar salarios calculados
print("Salario del empleado normal:", salario_empleado_normal)
print("Salario del asistente:", salario_asistente)
