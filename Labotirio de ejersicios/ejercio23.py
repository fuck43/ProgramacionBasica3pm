class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Las matrices deben tener el mismo tamaño")
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Las matrices deben tener el mismo tamaño")
        return Matrix([[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda")
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)

    def transpose(self):
        return Matrix([[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)])

# Ejemplo de uso
A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matriz A:")
print(A)
print("\nMatriz B:")
print(B)

print("\nSuma de A y B:")
print(A + B)

print("\nResta de A y B:")
print(A - B)

print("\nMultiplicación de A y B:")
print(A * B)

print("\nTransposición de A:")
print(A.transpose())
