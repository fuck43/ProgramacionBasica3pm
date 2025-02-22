def suma_serie(serie):
    """
    Calcula la suma de una serie numérica dada como lista.
    :param serie: Lista de números.
    :return: Suma de los elementos de la serie.
    """
    return sum(serie)

# Ejemplo de uso
serie = [1, 2, 3, 4, 5]
resultado = suma_serie(serie)
print(f"La suma de la serie es: {resultado}")
