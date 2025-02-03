# Pedir al usuario el límite superior
limite = int(input("Ingrese el límite superior: "))

# Generar listas de números pares e impares
pares = [num for num in range(0, limite + 1, 2)]
impares = [num for num in range(1, limite + 1, 2)]

# Mostrar los resultados
print(f"Números pares hasta {limite}: {pares}")
print(f"Números impares hasta {limite}: {impares}")
#va indicar si nes par o inpar