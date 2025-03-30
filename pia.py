def invertir_cadena(cadena):
    resultado = ""  # Inicializar la variable resultado
    indice = len(cadena)  # Obtener la longitud de la cadena

    while indice > 0:
        resultado += cadena[indice - 1]  # Acceder al último carácter disponible
        indice -= 1  # Decrementar el índice

    return resultado

palabra = input("Ingresa una palabra: ")

print("Palabra invertida:", invertir_cadena(palabra))

 



