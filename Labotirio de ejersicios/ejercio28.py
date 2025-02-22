class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("El monto debe ser mayor a 0.")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")
        elif monto > self.saldo:
            print("Fondos insuficientes.")
        else:
            print("El monto debe ser mayor a 0.")

    def consultar_saldo(self):
        print(f"Saldo actual: ${self.saldo:.2f}")

def menu():
    nombre = input("Ingrese su nombre: ")
    cuenta = CuentaBancaria(nombre)

    while True:
        print("\n--- MENÚ BANCO ---")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Consultar saldo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)
        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == "3":
            cuenta.consultar_saldo()
        elif opcion == "4":
            print("Saliendo del sistema bancario...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
