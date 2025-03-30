# Solicitar entrada al usuario
numeros = list(map(float, input("Ingrese una lista de números separados por espacio: ").split()))

# Llamar a la función y mostrar los resultados
promedio, mediana, desviacion = calcular_estadisticas(*numeros)
print(f"Promedio: {promedio:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desviación estándar: {desviacion:.2f}")
