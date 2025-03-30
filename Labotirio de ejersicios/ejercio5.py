def factorial(numero):
    if numero < 0:  
        return   # ✅ Corrección: El factorial de 0 es 1.
    
    # ❌ Eliminado: `elif numero == 0 or numero == 1:` porque es redundante.
    elif numero == 1:
        return   # ✅ Corrección: Factorial de 1 también es 1.

    resultado = 1  # ✅ Se inicializa correctamente antes del `for`
    
    for i in range(2, numero + 1):  
        resultado *= i  # ✅ Corrección: `resultado *= i` estaba bien, solo mejoramos claridad.

    return resultado  # ✅ Retornamos el resultado correctamente.

# Solicitar número al usuario
numero = int(input("Ingrese el número para calcular el factorial: "))

# Mostrar el resultado
print(f"El factorial de {numero} es {factorial(numero)}")



   
