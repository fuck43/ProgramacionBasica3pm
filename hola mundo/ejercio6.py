def interes_compuesto(P, r, t, n=1):
    A = P * (1 + r / n) ** (n * t)
    return A

# Datos de ejemplo
P = float(input("Ingrese el capital inicial: "))
r = float(input("Ingrese la tasa de interés anual (en porcentaje): ")) / 100
t = float(input("Ingrese el tiempo en años: "))
n = int(input("Ingrese el número de veces que se capitaliza por año (ej. 1 = anual, 12 = mensual): "))

monto_final = interes_compuesto(P, r, t, n)
print(f"El monto final después de {t} años será: {monto_final:.2f}")
#lo def y luego trasladar la formula del interes compuestos