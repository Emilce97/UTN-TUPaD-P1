# 1) Programa que imprime números del 0 al 100 en orden creciente
def imprimir_numeros_creciente():
    """Imprime los números enteros desde 0 hasta 100, uno por línea."""
    for numero in range(101):  # range(101) genera números de 0 a 100
        print(numero)

# 2) Programa que cuenta los dígitos de un número entero
def contar_digitos(numero):
    """Cuenta la cantidad de dígitos de un número entero.

    Args:
        numero: El número entero a analizar.

    Returns:
        La cantidad de dígitos del número.
    """
    numero_str = str(abs(numero))  # Convierte a string y maneja negativos
    return len(numero_str)

# 3) Programa que suma números entre dos valores dados
def sumar_numeros_entre(valor1, valor2):
    """Suma los números enteros entre dos valores dados (excluyéndolos).

    Args:
        valor1: El primer valor.
        valor2: El segundo valor.

    Returns:
        La suma de los números entre valor1 y valor2.
    """
    if valor1 > valor2:  # Asegura que el rango sea ascendente
        valor1, valor2 = valor2, valor1  # Intercambia los valores
    suma = 0
    for numero in range(valor1 + 1, valor2):  # Excluye valor1 y valor2
        suma += numero
    return suma

# 4) Programa que suma números ingresados por el usuario hasta que se ingresa un 0
def sumar_numeros_usuario():
    """Suma números enteros ingresados por el usuario hasta que se ingresa un 0.

    Returns:
        La suma de los números ingresados.
    """
    suma = 0
    while True:
        numero = int(input("Ingrese un número entero (0 para terminar): "))
        if numero == 0:
            break  # Termina el bucle si se ingresa 0
        suma += numero
    return suma

# 5) Juego de adivinar un número aleatorio
import random  # Importa el módulo random para generar números aleatorios

def adivinar_numero():
    """Juego en el que el usuario adivina un número aleatorio entre 0 y 9."""
    numero_secreto = random.randint(0, 9)  # Genera un número aleatorio entre 0 y 9
    intentos = 0
    print("Adivina un número entre 0 y 9.")
    while True:
        intento = int(input("Ingrese su intento: "))
        intentos += 1
        if intento == numero_secreto:
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
            break  # Termina el bucle cuando se adivina el número
        else:
            print("Incorrecto. Intente nuevamente.")

# 6) Programa que imprime números pares del 0 al 100 en orden decreciente
def imprimir_pares_decreciente():
    """Imprime los números pares desde 100 hasta 0 en orden decreciente."""
    for numero in range(100, -1, -2):  # range(inicio, fin, paso)
        print(numero)

# 7) Programa que calcula la suma de números del 0 al número ingresado por el usuario
def sumar_numeros_hasta(numero):
    """Calcula la suma de los números enteros desde 0 hasta un número dado.

    Args:
        numero: El número entero positivo hasta el cual sumar.

    Returns:
        La suma de los números desde 0 hasta numero.
    """
    if numero < 0:
        return 0  # Si el número es negativo, retorna 0
    suma = 0
    for i in range(numero + 1):
        suma += i
    return suma

# Llamadas a las funciones para ejecutar los programas
print("Ejercicio 1: Números del 0 al 100 creciente")
imprimir_numeros_creciente()

print("\nEjercicio 2: Contar dígitos de un número")
numero_usuario = int(input("Ingrese un número entero: "))
cantidad_digitos = contar_digitos(numero_usuario)
print(f"El número {numero_usuario} tiene {cantidad_digitos} dígitos.")

print("\nEjercicio 3: Sumar números entre dos valores")
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
suma_entre_valores = sumar_numeros_entre(valor1, valor2)
print(f"La suma de los números entre {valor1} y {valor2} es: {suma_entre_valores}")

print("\nEjercicio 4: Sumar números ingresados por el usuario hasta 0")
suma_usuario = sumar_numeros_usuario()
print(f"La suma de los números ingresados es: {suma_usuario}")

print("\nEjercicio 5: Juego de adivinar un número")
adivinar_numero()

print("\nEjercicio 6: Números pares del 0 al 100 decreciente")
imprimir_pares_decreciente()

print("\nEjercicio 7: Sumar números del 0 al número ingresado")
numero_usuario_suma = int(input("Ingrese un número entero positivo: "))
suma_hasta_numero = sumar_numeros_hasta(numero_usuario_suma)
print(f"La suma de los números desde 0 hasta {numero_usuario_suma} es: {suma_hasta_numero}")
 8) Programa que clasifica 100 números enteros ingresados por el usuario
def clasificar_numeros():
    """Clasifica 100 números enteros ingresados por el usuario, indicando cuántos son pares,
    impares, positivos y negativos.
    """
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0

    for _ in range(100):  # Usa un bucle for para pedir 100 números
        numero = int(input("Ingrese un número entero: "))

        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1

    print("\nResultados:")
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Números positivos: {positivos}")
    print(f"Números negativos: {negativos}")


# 9) Programa que calcula la media de 100 números enteros ingresados por el usuario
def calcular_media():
    """Calcula la media de 100 números enteros ingresados por el usuario."""
    suma = 0
    for _ in range(100):  # Pide 100 números
        numero = float(input("Ingrese un número entero: "))  # Usar float para mayor precisión
        suma += numero
    media = suma / 100 if 100 > 0 else 0 # Calcula la media. Evita dividir por cero.
    print(f"La media de los números ingresados es: {media}")


# 10) Programa que invierte el orden de los dígitos de un número
def invertir_digitos(numero):
    """Invierte el orden de los dígitos de un número entero.

    Args:
        numero: El número entero a invertir.

    Returns:
        El número con los dígitos invertidos.
    """
    numero_str = str(abs(numero))  # Convierte el número a string y maneja negativos
    numero_invertido_str = numero_str[::-1]  # Invierte el string
    numero_invertido = int(numero_invertido_str)  # Convierte el string invertido a entero
    if numero < 0:
        numero_invertido *= -1 # Restaura el signo negativo si el número original era negativo
    return numero_invertido


# Llamadas a las funciones para ejecutar los programas
print("Ejercicio 8: Clasificar 100 números")
clasificar_numeros()

print("\nEjercicio 9: Calcular la media de 100 números")
calcular_media()

print("\nEjercicio 10: Invertir dígitos de un número")
numero_usuario = int(input("Ingrese un número entero: "))
numero_invertido = invertir_digitos(numero_usuario)
print(f"El número invertido es: {numero_invertido}")