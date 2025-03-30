# Programa para analizar un texto ingresado por el usuario
import string

def analizar_texto(texto):
    """
    Función que analiza un texto y devuelve:
    - Número total de palabras
    - Cantidad de palabras únicas
    - Frecuencia de cada palabra
    - Palabra más frecuente y su frecuencia
    """
    # Convertir el texto a minúsculas y eliminar signos de puntuación
    texto = texto.lower().translate(str.maketrans('', '', string.punctuation))
    
    # Dividir el texto en palabras
    palabras = texto.split()
    
    # Contar el número total de palabras
    total_palabras = len(palabras)
    
    # Obtener la cantidad de palabras únicas usando un conjunto
    palabras_unicas = set(palabras)
    total_palabras_unicas = len(palabras_unicas)
    
    # Contar la frecuencia de cada palabra usando un diccionario
    frecuencia_palabras = {}
    for palabra in palabras:
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
    
    # Determinar la palabra más frecuente
    palabra_mas_frecuente = max(frecuencia_palabras, key=frecuencia_palabras.get)
    frecuencia_maxima = frecuencia_palabras[palabra_mas_frecuente]
    
    # Imprimir los resultados
    print(f"Número total de palabras: {total_palabras}")
    print(f"Número de palabras únicas: {total_palabras_unicas}")
    print("Frecuencia de palabras:")
    for palabra, frecuencia in frecuencia_palabras.items():
        print(f"  {palabra}: {frecuencia}")
    print(f"Palabra más frecuente: '{palabra_mas_frecuente}' con {frecuencia_maxima} apariciones.")

# Solicitar al usuario que ingrese un texto
if __name__ == "__main__":
    texto_usuario = input("Ingrese un texto para analizar: ")
    analizar_texto(texto_usuario)