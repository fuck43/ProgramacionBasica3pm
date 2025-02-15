str1 = input("Ingrese la palabra: ").strip()  # Se eliminan espacios innecesarios
vocales = 0
consonantes = 0

for i in str1:
    if i in 'aeiouAEIOU':  # Comparación simplificada
        vocales += 1
    elif i.isalpha():  # Verifica si es una letra para contar consonantes
        consonantes += 1

print("Total de vocales:", vocales)
print("Total de consonantes:", consonantes)
