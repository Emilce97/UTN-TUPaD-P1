#TRABAJO PRÁCTICO: RECURSIVIDAD
#ESTUDIANTE: EMILCE SPITAL
import sys
sys.setrecursionlimit(2000) 

# Ejercicio 1: Calcular el factorial de un número
def factorial(n):
    """
    Calcula el factorial de un número entero positivo de forma recursiva.
    El factorial de n (n!) es el producto de todos los enteros positivos desde 1 hasta n.
    Caso base: factorial(0) = 1
    Caso recursivo: factorial(n) = n * factorial(n-1)
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ejercicio 2: Calcular el valor de la serie de Fibonacci
def fibonacci(n):
    """
    Calcula el valor de la serie de Fibonacci en la posición indicada de forma recursiva.
    La serie de Fibonacci comienza con 0 y 1, y cada número posterior es la suma de los dos anteriores.
    Ej: 0, 1, 1, 2, 3, 5, 8, ...
    Caso base: fibonacci(0) = 0, fibonacci(1) = 1
    Caso recursivo: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejercicio 3: Calcular la potencia de un número
def potencia(base, exponente):
    """
    Calcula la potencia de un número base elevado a un exponente de forma recursiva.
    Utiliza la fórmula n^m = n * n^(m-1).
    Caso base: n^0 = 1
    Caso recursivo: n^m = n * n^(m-1)
    """
    if exponente == 0:
        return 1
    elif exponente < 0:
        # Manejo de exponentes negativos: a^(-b) = 1 / a^b
        return 1 / potencia(base, -exponente)
    else:
        return base * potencia(base, exponente - 1)

# Ejercicio 4: Convertir un número decimal a binario
def decimal_a_binario(n):
    """
    Convierte un número entero positivo en base decimal a su representación binaria
    como una cadena de texto de forma recursiva.
    Procedimiento:
    1. Dividir el número por 2.
    2. Guardar el resto (0 o 1).
    3. Repetir el proceso con el cociente hasta que llegue a 0.
    4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
    Caso base: si n es 0, la representación binaria es "0".
    """
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        # El resto de la división es el último dígito binario (0 o 1)
        # El cociente se usa para la siguiente llamada recursiva
        return decimal_a_binario(n // 2) + str(n % 2)

# Ejercicio 5: Verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    """
    Verifica si una cadena de texto es un palíndromo de forma recursiva.
    Un palíndromo es una palabra que se lee igual de izquierda a derecha que de derecha a izquierda.
    La palabra no debe contener espacios ni tildes.
    No se usa [::-1] ni reversed().
    Caso base: si la palabra tiene 0 o 1 carácter, es un palíndromo (True).
    Caso recursivo: compara el primer y último carácter; si son iguales,
    llama recursivamente con la subcadena sin esos caracteres.
    """
    palabra = palabra.lower() # Convertir a minúsculas para ignorar mayúsculas/minúsculas
    if len(palabra) <= 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            # Llama recursivamente con la subcadena que excluye el primer y último carácter
            return es_palindromo(palabra[1:-1])
        else:
            return False

# Ejercicio 6: Sumar los dígitos de un número
def suma_digitos(n):
    """
    Calcula la suma de todos los dígitos de un número entero positivo de forma recursiva.
    Restricciones: No se puede convertir el número a string. Usar operaciones matemáticas (%, //) y recursión.
    Caso base: si n es 0, la suma es 0.
    Caso recursivo: suma el último dígito (n % 10) con la suma de los dígitos del resto del número (n // 10).
    """
    if n == 0:
        return 0
    else:
        # n % 10 obtiene el último dígito
        # n // 10 obtiene el número sin el último dígito
        return (n % 10) + suma_digitos(n // 10)

# Ejercicio 7: Contar bloques de una pirámide
def contar_bloques(n):
    """
    Calcula el total de bloques necesarios para construir una pirámide de n niveles
    de forma recursiva. En el nivel más bajo hay n bloques, luego n-1, hasta 1.
    Caso base: si n es 0, no se necesitan bloques (0).
    Caso recursivo: n + el total de bloques de una pirámide de n-1 niveles.
    """
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

# Ejercicio 8: Contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    """
    Cuenta cuántas veces aparece un dígito específico (entre 0 y 9)
    dentro de un número entero positivo de forma recursiva.
    Restricciones: Idealmente usar operaciones matemáticas (%, //) y recursión.
    Caso base: si el número es 0, el dígito no puede aparecer más (0).
    Caso recursivo:
    - Compara el último dígito del número con el dígito buscado.
    - Suma 1 si coinciden, 0 si no.
    - Llama recursivamente con el número sin el último dígito (numero // 10).
    """
    if numero == 0:
        # Caso base: si el número es 0, el dígito ya no puede aparecer.
        # Es importante para que la recursión termine.
        return 0
    else:
        ultimo_digito = numero % 10
        # Comprueba si el último dígito es el que buscamos
        contador_actual = 1 if ultimo_digito == digito else 0
        
        # Suma el contador actual con el resultado de la llamada recursiva
        # al número sin el último dígito.
        return contador_actual + contar_digito(numero // 10, digito)

# --- Bloque Principal para Demostraciones ---
if __name__ == "__main__":
    print("--- Demostraciones de Funciones Recursivas ---")
    print("\n" + "=" * 50)

    # Demostración Ejercicio 1: Factorial
    print("EJERCICIO 1: Cálculo de Factorial")
    try:
        num_factorial = int(input("Ingrese un número entero positivo para calcular factoriales hasta él: "))
        if num_factorial < 0:
            print("Por favor, ingrese un número no negativo.")
        else:
            for i in range(1, num_factorial + 1):
                print(f"El factorial de {i} es: {factorial(i)}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")
    print("=" * 50)

    # Demostración Ejercicio 2: Serie de Fibonacci
    print("\n" + "=" * 50)
    print("EJERCICIO 2: Serie de Fibonacci")
    try:
        pos_fibonacci = int(input("Ingrese la posición hasta la cual desea ver la serie de Fibonacci: "))
        if pos_fibonacci < 0:
            print("Por favor, ingrese una posición no negativa.")
        else:
            print(f"Serie de Fibonacci hasta la posición {pos_fibonacci}:")
            for i in range(pos_fibonacci + 1):
                print(f"F({i}) = {fibonacci(i)}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")
    print("=" * 50)

    # Demostración Ejercicio 3: Potencia
    print("\n" + "=" * 50)
    print("EJERCICIO 3: Cálculo de Potencia")
    try:
        base_pot = float(input("Ingrese la base: "))
        exp_pot = int(input("Ingrese el exponente (entero): "))
        print(f"{base_pot} elevado a la {exp_pot} es: {potencia(base_pot, exp_pot)}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números válidos.")
    print("=" * 50)

    # Demostración Ejercicio 4: Decimal a Binario
    print("\n" + "=" * 50)
    print("EJERCICIO 4: Conversión Decimal a Binario")
    try:
        num_decimal = int(input("Ingrese un número entero positivo para convertir a binario: "))
        if num_decimal < 0:
            print("Por favor, ingrese un número positivo.")
        elif num_decimal == 0:
             print(f"El número {num_decimal} en binario es: 0")
        else:
            print(f"El número {num_decimal} en binario es: {decimal_a_binario(num_decimal)}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")
    print("=" * 50)

    # Demostración Ejercicio 5: Es Palíndromo
    print("\n" + "=" * 50)
    print("EJERCICIO 5: Verificación de Palíndromo")
    palabra_palindromo = input("Ingrese una palabra (sin espacios ni tildes) para verificar si es un palíndromo: ")
    if es_palindromo(palabra_palindromo):
        print(f"La palabra '{palabra_palindromo}' ES un palíndromo.")
    else:
        print(f"La palabra '{palabra_palindromo}' NO ES un palíndromo.")
    print("=" * 50)

    # Demostración Ejercicio 6: Suma de Dígitos
    print("\n" + "=" * 50)
    print("EJERCICIO 6: Suma de Dígitos de un Número")
    try:
        num_suma_digitos = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
        if num_suma_digitos < 0:
            print("Por favor, ingrese un número positivo.")
        else:
            print(f"La suma de los dígitos de {num_suma_digitos} es: {suma_digitos(num_suma_digitos)}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")
    print("=" * 50)

    # Demostración Ejercicio 7: Contar Bloques de Pirámide
    print("\n" + "=" * 50)
    print("EJERCICIO 7: Conteo de Bloques de Pirámide")
    try:
        nivel_base = int(input("Ingrese el número de bloques en el nivel más bajo de la pirámide: "))
        if nivel_base < 0:
            print("Por favor, ingrese un número no negativo para los bloques.")
        else:
            print(f"Para una pirámide con {nivel_base} bloques en la base, se necesitan un total de {contar_bloques(nivel_base)} bloques.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")
    print("=" * 50)

    # Demostración Ejercicio 8: Contar Dígito en Número
    print("\n" + "=" * 50)
    print("EJERCICIO 8: Conteo de Dígitos en un Número")
    try:
        num_contar = int(input("Ingrese un número entero positivo: "))
        digito_buscar = int(input("Ingrese el dígito a buscar (0-9): "))
        if not (0 <= digito_buscar <= 9):
            print("Por favor, ingrese un dígito entre 0 y 9.")
        elif num_contar < 0:
            print("Por favor, ingrese un número positivo.")
        else:
            # Si el número ingresado es 0 y el dígito buscado también es 0, el resultado es 1.
            # La función maneja el 0 de manera que contar_digito(0, 0) devuelve 0.
            # Para el caso especial de contar el dígito 0 en el número 0, podríamos añadir una condición específica
            # fuera de la función recursiva si el usuario espera 1 en ese caso.
            # Sin embargo, la definición de la función recursiva para el 0 es que no tiene más dígitos.
            if num_contar == 0 and digito_buscar == 0:
                 print(f"El dígito {digito_buscar} aparece 1 vez en el número {num_contar}.")
            else:
                 print(f"El dígito {digito_buscar} aparece {contar_digito(num_contar, digito_buscar)} veces en el número {num_contar}.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números enteros válidos.")
    print("=" * 50)

    print("\n--- Fin de Demostraciones ---")
