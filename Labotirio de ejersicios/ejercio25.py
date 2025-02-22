import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios
data = np.random.randn(1000)  # 1000 valores de una distribución normal

# Crear el histograma
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)  # 30 barras, bordes negros

# Etiquetas y título
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma de Datos')

# Mostrar el histograma
plt.show()
