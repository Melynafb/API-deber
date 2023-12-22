import requests

url = "https://dummy.restapiexample.com/api/v1/employees"
empleados = requests.get(url)
data = empleados.json()

numer_empleados = len(data["data"])

sueldo = [float(emp["employee_salary"]) for emp in data["data"]]
promedio_salario = sum(sueldo) / numer_empleados

edades = [int(emp["employee_age"]) for emp in data["data"]]
promedio_edad = sum(edades) / numer_empleados

sueldo_minimo = min(sueldo)
sueldo_maximo = max(sueldo)

edad_minima = min(edades)
edad_maxima = max(edades)


print(f"Cantidad de empleados: {numer_empleados}")
print(f"Promedio de salario: {promedio_salario}")
print(f"Promedio de edad: {promedio_edad}")
print(f"Salario mínimo: {sueldo_minimo}")
print(f"Salario máximo: {sueldo_maximo}")
print(f"Edad mínima: {edad_minima}")
print(f"Edad máxima: {edad_maxima}")



