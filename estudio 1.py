def fibonacci(n):
    nums = []  # Lista para almacenar los números de Fibonacci
    a, b = 0, 1  # Inicializar los dos primeros números de la secuencia
    
    for i in range(n):
        nums.append(a)  # Agregar el número actual a la lista
        a, b = b, a + b  # Actualizar los valores de a y b
    
    return nums

# Solicitar un número al usuario
numero = int(input("Ingrese la cantidad de números en la secuencia Fibonacci: "))

# Mostrar la secuencia de Fibonacci
print(f"Los primeros {numero} números de Fibonacci son: {fibonacci(numero)}")


