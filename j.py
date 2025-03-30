def es_palindromo(numero):
    # Normalizamos la palabra para evitar problemas con mayúsculas/minúsculas y espacios
    numero = numero.replace(" ", "").lower()
    
    # Verificamos si la palabra es igual a su reverso
    return numero == numero[::-1]

# Solicitar una palabra al usuario
numero = input("Ingrese una palabra para verificar si es un palíndromo: ")

# Verificar si es palíndromo y mostrar el resultado
if es_palindromo(numero):
    print(f"La palabra '{numero}' es un palíndromo.")
else: 'b
    print(f"La palabra '{numero}' no es un palíndromo.")
