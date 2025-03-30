import conversor

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\nConversor de Unidades")
    print("1. Convertir Kilómetros a Millas")
    print("2. Convertir Celsius a Fahrenheit")
    print("3. Convertir Litros a Galones")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        km = float(input("Ingrese la cantidad en kilómetros: "))
        resultado = conversor.km_a_millas(km)
        print(f"{km} kilómetros son {resultado:.2f} millas.")
    
    elif opcion == "2":
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        resultado = conversor.celsius_a_fahrenheit(celsius)
        print(f"{celsius}°C son {resultado:.2f}°F.")

    elif opcion == "3":
        litros = float(input("Ingrese la cantidad en litros: "))
        resultado = conversor.litros_a_galones(litros)
        print(f"{litros} litros son {resultado:.2f} galones.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Inténtelo de nuevo.")  

def km_a_millas(km):
    """
    Convierte kilómetros a millas.
    1 kilómetro = 0.621371 millas.
    """
    return km * 0.621371

def celsius_a_fahrenheit(celsius):
    """
    Convierte grados Celsius a Fahrenheit.
    Fórmula: (°C × 9/5) + 32 = °F
    """
    return (celsius * 9/5) + 32

def litros_a_galones(litros):
    """
    Convierte litros a galones.
    1 litro = 0.264172 galones.
    """
    return litros * 0.264172