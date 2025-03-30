import random

# Función para generar una lista de números aleatorios
def generar_lista(tamano, rango_inferior, rango_superior):
    return [random.randint(rango_inferior, rango_superior) for _ in range(tamano)]

# Implementación del algoritmo Quicksort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    menores = [x for x in lista[1:] if x <= pivot]
    mayores = [x for x in lista[1:] if x > pivot]
    return quicksort(menores) + [pivot] + quicksort(mayores)

# Función de búsqueda binaria
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio  # Devuelve el índice donde se encuentra el objetivo
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # Si el número no se encuentra, devuelve -1

# Función principal
def main():
    tamano_lista = int(input("Ingresa el tamaño de la lista: "))
    rango_inferior = int(input("Ingresa el rango inferior de los números: "))
    rango_superior = int(input("Ingresa el rango superior de los números: "))

    # Generamos la lista aleatoria
    lista = generar_lista(tamano_lista, rango_inferior, rango_superior)

    print("\nLista original:")
    print(lista)

    # Ordenamos la lista con Quicksort
    lista_ordenada = quicksort(lista)

    print("\nLista ordenada:")
    print(lista_ordenada)

    # Realizamos la búsqueda binaria
    numero_a_buscar = int(input("\nIngresa el número que deseas buscar: "))
    resultado_busqueda = busqueda_binaria(lista_ordenada, numero_a_buscar)

    if resultado_busqueda != -1:
        print(f"\nEl número {numero_a_buscar} fue encontrado en el índice {resultado_busqueda}.")
    else:
        print(f"\nEl número {numero_a_buscar} no se encuentra en la lista.")

if __name__ == "__main__":
    main()
