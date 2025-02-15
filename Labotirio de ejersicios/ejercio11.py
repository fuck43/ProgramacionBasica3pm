def es_palindromo(cadena):
    a = 0
    b = len(cadena) - 1  # Última posición

    for i in range(len(cadena) // 2):  # Solo la mitad de la palabra
        if cadena[a] != cadena[b]:  # Comparación de extremos
            return False
        a += 1
        b -= 1

    return True


palabra = input("Ingrese una palabra: ").lower().replace(" ", "")  # Convierte a minúsculas y quita espacios


if es_palindromo(palabra):
    print("Sí es un palíndromo")
else:
    print("No es un palíndromo")