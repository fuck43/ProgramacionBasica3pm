# Programa para gestionar contactos con tuplas y estructuras anidadas

def agregar_contacto(agenda, nombre, numero, correo):
    """Agrega un nuevo contacto a la agenda."""
    contacto = (nombre, numero, correo)
    agenda.append(contacto)
    print(f"Contacto {nombre} agregado correctamente.")

def buscar_contacto(agenda, nombre):
    """Busca un contacto por nombre y muestra sus detalles."""
    for contacto in agenda:
        if contacto[0].lower() == nombre.lower():
            print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")
            return
    print("Contacto no encontrado.")

def listar_contactos(agenda):
    """Lista todos los contactos en orden alfabético."""
    agenda_ordenada = sorted(agenda, key=lambda x: x[0].lower())
    print("Lista de contactos:")
    for contacto in agenda_ordenada:
        print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")

def main():
    """Función principal del programa."""
    agenda = []
    
    while True:
        print("\nGestión de Contactos")
        print("1. Agregar Contacto")
        print("2. Buscar Contacto")
        print("3. Listar Contactos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            numero = input("Ingrese el número: ")
            correo = input("Ingrese el correo: ")
            agregar_contacto(agenda, nombre, numero, correo)
        elif opcion == "2":
            nombre = input("Ingrese el nombre a buscar: ")
            buscar_contacto(agenda, nombre)
        elif opcion == "3":
            listar_contactos(agenda)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()