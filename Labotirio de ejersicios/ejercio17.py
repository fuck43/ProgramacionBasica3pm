class Pila:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if not self.esta_vacia() else None
    
    def esta_vacia(self):
        return len(self.items) == 0

class Cola:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0) if not self.esta_vacia() else None
    
    def esta_vacia(self):
        return len(self.items) == 0

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' -> ')
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
pila = Pila()
pila.push(1)
pila.push(2)
print("Pila después de push:", pila.items)
print("Elemento eliminado de la pila:", pila.pop())

cola = Cola()
cola.enqueue(3)
cola.enqueue(4)
print("Cola después de enqueue:", cola.items)
print("Elemento eliminado de la cola:", cola.dequeue())

lista = ListaEnlazada()
lista.insertar(10)
lista.insertar(20)
print("Lista enlazada:")
lista.mostrar()
