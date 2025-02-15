num = int(input("Ingrese un número: "))
divisor = int(input("Ingrese otro número para verificar múltiplo: "))

# Verificar si es par o impar
if num % 2 == 0:
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")

# Verificar si es múltiplo del divisor
if num % divisor == 0:
    print(f"El número {num} es múltiplo de {divisor}.")
else:
    print(f"El número {num} no es múltiplo de {divisor}.")
    #lo que va aser es comparar si es disible entre 2 y la ota verficara si es multiplo diviendo por el divisor 
