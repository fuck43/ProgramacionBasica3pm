def fibonacci(numero):
    numes = []  # Lista donde se guardarán los números de Fibonacci
    a, b = 0, 1  # Inicia los dos primeros números de la secuencia
    for i in range(numero):  # Bucle para generar los primeros 'numero' números
        numes.append(a)  # Añade el número 'a' a la lista
        a, b = b, a + b  # Calcula el siguiente número en la secuencia
    return numes

# Pedir número al usuario
numero = int(input("Ingrese el número de términos de la secuencia de Fibonacci: "))

# Imprimir la secuencia de Fibonacci
print(f"Los primeros {numero} números de Fibonacci son: {fibonacci(numero)}")

