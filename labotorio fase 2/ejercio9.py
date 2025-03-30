"""
Módulo que implementa funciones básicas de cálculo siguiendo un paradigma estructurado.
"""

def suma(a, b):
    """Suma dos números y retorna el resultado."""
    return a + b

def resta(a, b):
    """Resta dos números y retorna el resultado."""
    return a - b

def multiplicacion(a, b):
    """Multiplica dos números y retorna el resultado."""
    return a * b

def division(a, b):
    """Divide dos números y maneja la división entre cero."""
    if b == 0:
        return "Error: División entre cero"
    return a / b 
"""
Módulo que contiene funciones de utilidad y ejemplos del paradigma imperativo.
"""

def factorial(n):
    """Calcula el factorial de un número de forma iterativa (imperativo)."""
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def es_par(numero):
    """Determina si un número es par o impar usando una estructura condicional."""
    if numero % 2 == 0:
        return True
    return False 

"""
Módulo que define una clase Persona con atributos y métodos (Paradigma POO).
"""

class Persona:
    def __init__(self, nombre, edad):
        """Constructor de la clase Persona."""
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        """Método para saludar."""
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."  
# main.py
"""
Punto de entrada del programa donde se integran los diferentes paradigmas.
"""

import calculadora
import utilidades
from persona import Persona

def main():
    """Función principal del programa."""
    
    # Uso del paradigma estructurado (llamando funciones)
    print("Suma de 5 + 3:", calculadora.suma(5, 3))
    print("Factorial de 5:", utilidades.factorial(5))
    
    # Uso del paradigma imperativo (control de flujo)
    numero = 7
    if utilidades.es_par(numero):
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

    # Uso del paradigma orientado a objetos
    persona1 = Persona("Carlos", 30)
    print(persona1.saludar())

if __name__ == "__main__":
    main()
