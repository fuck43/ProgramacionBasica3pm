def convertir_longitud(valor, unidad_origen, unidad_destino):
    # Factores de conversión a metros
    factores = {
        "m": 1, "km": 1000, "cm": 0.01, "mm": 0.001,
        "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.34
    }
    
    if unidad_origen in factores and unidad_destino in factores:
        valor_metros = valor * factores[unidad_origen]
        return valor_metros / factores[unidad_destino]
    else:
        return None

def convertir_peso(valor, unidad_origen, unidad_destino):
    # Factores de conversión a kilogramos
    factores = {
        "kg": 1, "g": 0.001, "mg": 0.000001, "lb": 0.453592, "oz": 0.0283495
    }
    
    if unidad_origen in factores and unidad_destino in factores:
        valor_kg = valor * factores[unidad_origen]
        return valor_kg / factores[unidad_destino]
    else:
        return None

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "C":
        return valor if unidad_destino == "C" else (valor * 9/5 + 32) if unidad_destino == "F" else (valor + 273.15) if unidad_destino == "K" else None
    elif unidad_origen == "F":
        return valor if unidad_destino == "F" else ((valor - 32) * 5/9) if unidad_destino == "C" else ((valor - 32) * 5/9 + 273.15) if unidad_destino == "K" else None
    elif unidad_origen == "K":
        return valor if unidad_destino == "K" else (valor - 273.15) if unidad_destino == "C" else ((valor - 273.15) * 9/5 + 32) if unidad_destino == "F" else None
    else:
        return None

def menu():
    while True:
        print("\n--- CONVERSOR DE UNIDADES ---")
        print("1. Longitud (m, km, cm, mm, in, ft, yd, mi)")
        print("2. Peso (kg, g, mg, lb, oz)")
        print("3. Temperatura (C, F, K)")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            valor = float(input("Ingrese el valor: "))
            unidad_origen = input("Unidad de origen: ").strip().lower()
            unidad_destino = input("Unidad de destino: ").strip().lower()
            resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
        elif opcion == "2":
            valor = float(input("Ingrese el valor: "))
            unidad_origen = input("Unidad de origen: ").strip().lower()
            unidad_destino = input("Unidad de destino: ").strip().lower()
            resultado = convertir_peso(valor, unidad_origen, unidad_destino)
        elif opcion == "3":
            valor = float(input("Ingrese el valor: "))
            unidad_origen = input("Unidad de origen (C, F, K): ").strip().upper()
            unidad_destino = input("Unidad de destino (C, F, K): ").strip().upper()
            resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
        elif opcion == "4":
            print("Saliendo del conversor...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            continue
        
        if resultado is not None:
            print(f"Resultado: {valor} {unidad_origen} = {resultado:.4f} {unidad_destino}")
        else:
            print("Unidades no válidas. Intente de nuevo.")

# Ejecutar el conversor
if __name__ == "__main__":
    menu()
