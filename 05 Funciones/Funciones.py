
#Trabajo práctico N° 6 "Funciones"
#Estudiante: Spital, Emilce

#1 Funcion para imprimir "Hola mundo"
def imprimir_hola_mundo(): 
    print ("Hola mundo") 
    # Llamada a la función desde el programa principal
imprimir_hola_mundo()

#2 Funcion para saludar al usuario
def saludar_al_usuario(nombre):
    return f"hola{nombre}"
# Llamada a la función desde el programa principal solicitando el nombre
nombre_usuario = input("Ingrese su nombre: ")
saludo = saludar_al_usuario(nombre_usuario)
print(f"hola {nombre_usuario}")

#3 Función para imprimir información personal
def informacion_personal(nombre, apellido, edad, residencia):
  """Recibe nombre, apellido, edad y residencia e imprime la información."""
  print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Pedir los datos al usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4. Calcular área y perímetro de un círculo
import math
def calcular_area_circulo(radio):
  """Recibe el radio de un círculo y devuelve su área."""
  return math.pi * radio**2

def calcular_perimetro_circulo(radio):
  """Recibe el radio de un círculo y devuelve su perímetro."""
  return 2 * math.pi * radio

radio_circulo = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio_circulo)
perimetro = calcular_perimetro_circulo(radio_circulo)
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")
print("-" * 20)

# 5. Convertir segundos a horas
def segundos_a_horas(segundos):
  """Recibe segundos y devuelve la cantidad de horas."""
  return segundos / 3600

segundos_totales = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos_totales)
print(f"{segundos_totales} segundos equivalen a {horas:.2f} horas.")
print("-" * 20)

# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
  """Recibe un número e imprime su tabla de multiplicar del 1 al 10."""
  print(f"Tabla de multiplicar del {numero}:")
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

numero_tabla = int(input("Ingrese el número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_tabla)
print("-" * 20)

# 7. Operaciones básicas
def operaciones_basicas(a, b):
  """Recibe dos números y devuelve una tupla con suma, resta, multiplicación y división."""
  suma = a + b
  resta = a - b
  multiplicacion = a * b
  if b != 0:
    division = a / b
  else:
    division = "No se puede dividir por cero"
  return suma, resta, multiplicacion, division

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(num1, num2)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")
print("-" * 20)

# 8. Calcular IMC
def calcular_imc(peso, altura):
  """Recibe peso en kg y altura en metros, devuelve el IMC."""
  if altura > 0:
    imc = peso / (altura ** 2)
    return imc
  else:
    return "La altura debe ser mayor que cero."

peso_usuario = float(input("Ingrese su peso en kilogramos: "))
altura_usuario = float(input("Ingrese su altura en metros: "))
imc_resultado = calcular_imc(peso_usuario, altura_usuario)
if isinstance(imc_resultado, str):
  print(imc_resultado)
else:
  print(f"Su Índice de Masa Corporal (IMC) es: {imc_resultado:.2f}")
print("-" * 20)

# 9. Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
  """Recibe temperatura en Celsius y devuelve su equivalente en Fahrenheit."""
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

celsius_temp = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit_temp = celsius_a_fahrenheit(celsius_temp)
print(f"{celsius_temp:.2f} grados Celsius equivalen a {fahrenheit_temp:.2f} grados Fahrenheit.")
print("-" * 20)

# 10. Calcular promedio
def calcular_promedio(a, b, c):
  """Recibe tres números y devuelve su promedio."""
  return (a + b + c) / 3

num_a = float(input("Ingrese el primer número para el promedio: "))
num_b = float(input("Ingrese el segundo número para el promedio: "))
num_c = float(input("Ingrese el tercer número para el promedio: "))
promedio = calcular_promedio(num_a, num_b, num_c)
print(f"El promedio de {num_a}, {num_b} y {num_c} es: {promedio:.2f}")

