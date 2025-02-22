import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Generar datos aleatorios
def generar_datos(n=100, media=50, desviacion=15):
    datos = np.random.normal(media, desviacion, n)  # Datos con distribución normal
    return datos

# Calcular estadísticas básicas
def calcular_estadisticas(datos):
    media = np.mean(datos)
    mediana = np.median(datos)
    moda = stats.mode(datos, keepdims=True)[0][0]
    varianza = np.var(datos, ddof=1)
    desviacion = np.std(datos, ddof=1)

    print("\n--- Estadísticas de los Datos ---")
    print(f"Media: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Moda: {moda:.2f}")
    print(f"Varianza: {varianza:.2f}")
    print(f"Desviación Estándar: {desviacion:.2f}")

# Visualizar datos con histograma
def graficar_datos(datos):
    plt.hist(datos, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
    plt.axvline(np.mean(datos), color='red', linestyle='dashed', linewidth=2, label="Media")
    plt.axvline(np.median(datos), color='green', linestyle='dashed', linewidth=2, label="Mediana")
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Datos Generados')
    plt.legend()
    plt.show()

# Función principal
def main():
    n = int(input("Ingrese el número de datos a generar: "))
    datos = generar_datos(n)
    calcular_estadisticas(datos)
    graficar_datos(datos)

# Ejecutar el análisis
if __name__ == "__main__":
    main()
