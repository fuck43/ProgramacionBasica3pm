# sistema_inventario.py

# Diccionario para almacenar los productos
inventario = {}

def agregar_producto(nombre, categoria, precio, cantidad):
    """Agrega un producto al inventario."""
    if nombre in inventario:
        print("El producto ya existe. Se actualizará la cantidad.")
        inventario[nombre]["cantidad"] += cantidad
    else:
        inventario[nombre] = {"categoria": categoria, "precio": precio, "cantidad": cantidad}
    print(f"Producto {nombre} agregado/modificado con éxito.")

def eliminar_producto(nombre):
    """Elimina un producto del inventario por su nombre."""
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto {nombre} eliminado con éxito.")
    else:
        print("El producto no existe en el inventario.")

def buscar_producto(nombre):
    """Busca un producto por nombre y muestra su información."""
    if nombre in inventario:
        producto = inventario[nombre]
        print(f"Nombre: {nombre}, Categoría: {producto['categoria']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("Producto no encontrado.")

def mostrar_productos_ordenados():
    """Muestra todos los productos ordenados por precio de menor a mayor."""
    productos_ordenados = sorted(inventario.items(), key=lambda x: x[1]['precio'])
    print("\nInventario ordenado por precio:")
    for nombre, datos in productos_ordenados:
        print(f"Nombre: {nombre}, Categoría: {datos['categoria']}, Precio: {datos['precio']}, Cantidad: {datos['cantidad']}")

def menu():
    """Menú interactivo para manejar el inventario."""
    while True:
        print("\n--- Sistema de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto")
        print("4. Mostrar productos ordenados por precio")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            agregar_producto(nombre, categoria, precio, cantidad)
        elif opcion == "2":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(nombre)
        elif opcion == "3":
            nombre = input("Nombre del producto a buscar: ")
            buscar_producto(nombre)
        elif opcion == "4":
            mostrar_productos_ordenados()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()