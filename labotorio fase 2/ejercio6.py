# Definición de la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        """
        Constructor de la clase Vehiculo
        :param marca: Marca del vehículo
        :param modelo: Modelo del vehículo
        :param anio: Año del vehículo
        :param precio: Precio del vehículo
        """
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def mostrar_informacion(self):
        """Muestra la información del vehículo"""
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Precio: ${self.precio}")


# Definición de la subclase Automovil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, numero_puertas):
        """
        Constructor de la clase Automovil
        :param numero_puertas: Número de puertas del automóvil
        """
        super().__init__(marca, modelo, anio, precio)
        self.numero_puertas = numero_puertas

    def mostrar_informacion(self):
        """Muestra la información del automóvil, incluyendo el número de puertas"""
        super().mostrar_informacion()
        print(f"Número de puertas: {self.numero_puertas}")


# Definición de la subclase Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, cilindrada):
        """
        Constructor de la clase Motocicleta
        :param cilindrada: Cilindrada de la motocicleta en cc
        """
        super().__init__(marca, modelo, anio, precio)
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        """Muestra la información de la motocicleta, incluyendo la cilindrada"""
        super().mostrar_informacion()
        print(f"Cilindrada: {self.cilindrada}cc")


# Pruebas de las clases
if __name__ == "__main__":
    auto = Automovil("Toyota", "Corolla", 2022, 25000, 4)
    moto = Motocicleta("Honda", "CBR500R", 2023, 7000, 500)
    
    print("Información del automóvil:")
    auto.mostrar_informacion()
    print("\nInformación de la motocicleta:")
    moto.mostrar_informacion()
