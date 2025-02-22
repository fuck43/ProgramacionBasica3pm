import json

# Diccionario para almacenar los contactos
agenda = {}

# Cargar contactos desde un archivo JSON (si existe)
def cargar_contactos():
    global agenda
    try:
        with open("agenda.json", "r") as file:
            agenda = json.load(file)
    except FileNotFoundError:
        agenda = {}

# Guardar contactos en un archivo JSON
def guardar_contactos():
    with open("agenda.json", "w") as file:
        json.dump(agenda, file, indent=4)

# Agregar un nuevo contacto
def agregar_contacto():
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()
    
    if nombre in agenda:
        print("El contacto ya existe.")
    else:
        agenda[nombre] = {"Teléfono": telefono, "Email": email}
        print(f"Contacto {nombre} agregado.")
        guardar_contactos()

# Buscar un contacto
def buscar_contacto():
    nombre = input("Ingrese el nombre a buscar: ").strip()
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['Teléfono']}")
        print(f"Email: {agenda[nombre]['Email']}")
    else:
        print("Contacto no encontrado.")

# Actualizar un contacto existente
def actualizar_contacto():
    nombre = input("Ingrese el nombre del contacto a actualizar: ").strip()
    if nombre in agenda:
        telefono = input("Nuevo teléfono (dejar en blanco para no cambiar): ").strip()
        email = input("Nuevo email (dejar en blanco para no cambiar): ").strip()
        
        if telefono:
            agenda[nombre]['Teléfono'] = telefono
        if email:
            agenda[nombre]['Email'] = email
        
        print(f"Contacto {nombre} actualizado.")
        guardar_contactos()
    else:
        print("Contacto no encontrado.")

# Eliminar un contacto
def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado.")
        guardar_contactos()
    else:
        print("Contacto no encontrado.")

# Mostrar todos los contactos
def mostrar_contactos():
    if not agenda:
        print("La agenda está vacía.")
    else:
        for nombre, info in agenda.items():
            print(f"\nNombre: {nombre}")
            print(f"Teléfono: {info['Teléfono']}")
            print(f"Email: {info['Email']}")

# Menú de la agenda
def menu():
    cargar_contactos()
    while True:
        print("\n--- AGENDA DE CONTACTOS ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            actualizar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            mostrar_contactos()
        elif opcion == "6":
            print("Saliendo de la agenda...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar la agenda
if __name__ == "__main__":
    menu()
