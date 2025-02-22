def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva

# Prueba
num = 5
print(f"Factorial de {num} es {factorial(num)}") 

def fibonacci(n):
    if n == 0:  # Caso base
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Llamadas recursivas

# Prueba
num = 6
print(f"Fibonacci({num}) es {fibonacci(num)}")

def suma_numeros(n):
    if n == 1:  # Caso base
        return 1
    else:
        return n + suma_numeros(n - 1)  # Llamada recursiva

# Prueba
num = 10
print(f"Suma de los primeros {num} números es {suma_numeros(num)}")
