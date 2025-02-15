import math
a = int(input("Ingrese el coeficiente cuadrático (a): "))
b = int(input("Ingrese el coeficiente lineal (b): "))
c = int(input("Ingrese el término constante (c): "))
d = b**2 - 4*a*c
if d < 0:
    print("No existen soluciones en los números reales.")
else:
    x1 = (-b + math.sqrt(d)) / (2*a)  
    print("Solución x1:", x1)
    print("Solución x2:", x2)
