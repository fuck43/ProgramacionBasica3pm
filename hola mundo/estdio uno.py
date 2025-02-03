
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

suma = num1 + num2
multiplicacion = num1 * num2
resta = num1 - num2
division = num1 / num2 if num2 != 0 else "No se puede dividir por 0"

print("Los resultados son:")
print(f"Suma: {suma}")
print(f"Multiplicación: {multiplicacion}")
print(f"Resta: {resta}")
print(f"División: {division}")