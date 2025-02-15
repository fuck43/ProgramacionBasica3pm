def busqueda_lineal(lista, objetivo):
    """Realiza una búsqueda lineal en la lista."""
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Retorna la posición del elemento encontrado
    return -1  # Retorna -1 si no se encuentra el elemento


def busqueda_binaria(lista, objetivo):
    """Realiza una búsqueda binaria en la lista ordenada."""
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista[medio] == objetivo:
            return medio  # Elemento encontrado
        elif lista[medio] < objetivo:
            izquierda = medio + 1  # Buscar en la mitad derecha
        else:
            derecha = medio - 1  # Buscar en la mitad izquierda
    
    return -1  # Retorna -1 si no se encuentra el elemento


# Ejemplo de uso
lista = [1, 3, 5, 7, 9, 11, 13, 15]
objetivo = 7

# Búsqueda lineal
pos_lineal = busqueda_lineal(lista, objetivo)
print(f"Búsqueda lineal: Elemento encontrado en la posición {pos_lineal}")

# Búsqueda binaria (requiere lista ordenada)
pos_binaria = busqueda_binaria(lista, objetivo)
print(f"Búsqueda binaria: Elemento encontrado en la posición {pos_binaria}")
