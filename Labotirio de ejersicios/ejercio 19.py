import random
uniformes = [random.uniform(1, 10) for _ in range(5)]
print("Distribución Uniforme:", uniformes)

normales = [random.gauss(0, 1) for _ in range(5)]
print("Distribución Normal:", normales)
 
exponencial = np.random.exponential(1.5, 5)
print("Distribución Exponencial:", exponencial) 

binomial = np.random.binomial(10, 0.5, 5)
print("Distribución Binomial:", binomial) 

pareto = np.random.pareto(2, 5)
print("Distribución de Pareto:", pareto)