# Implementación del algoritmo Mergesort en Python

def merge_sort(lista):
    """
    Función que implementa el algoritmo Mergesort para ordenar una lista.
    """
    if len(lista) > 1:
        # Encontrar el punto medio de la lista
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        # Llamada recursiva a merge_sort en ambas mitades
        merge_sort(izquierda)
        merge_sort(derecha)

        # Variables auxiliares para el proceso de merge
        i = j = k = 0
        
        # Mezclar las listas izquierda y derecha ordenadamente
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Copiar los elementos restantes de izquierda, si los hay
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Copiar los elementos restantes de derecha, si los hay
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

# Solicitar al usuario una lista de números
entrada = input("Ingrese una lista de números separados por espacio: ")
lista_numeros = list(map(int, entrada.split()))

# Mostrar la lista antes del ordenamiento
print("Lista antes de ordenar:", lista_numeros)

# Aplicar Mergesort
merge_sort(lista_numeros)

# Mostrar la lista después del ordenamiento
print("Lista después de ordenar:", lista_numeros)