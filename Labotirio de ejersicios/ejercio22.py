import random

def lanzar_dado():
    return random.randint(1, 6)

def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

# Simulación
resultado_dado = lanzar_dado()
resultado_moneda = lanzar_moneda()

print(f"Resultado del dado: {resultado_dado}")
print(f"Resultado de la moneda: {resultado_moneda}")
