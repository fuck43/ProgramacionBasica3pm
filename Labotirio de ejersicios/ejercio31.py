import turtle

def sierpinski(lado, nivel):
    if nivel == 0:
        for _ in range(3):
            turtle.forward(lado)
            turtle.left(120)
    else:
        sierpinski(lado / 2, nivel - 1)  # Triángulo izquierdo
        turtle.forward(lado / 2)
        sierpinski(lado / 2, nivel - 1)  # Triángulo derecho
        turtle.backward(lado / 2)
        turtle.left(60)
        turtle.forward(lado / 2)
        turtle.right(60)
        sierpinski(lado / 2, nivel - 1)  # Triángulo superior
        turtle.left(60)
        turtle.backward(lado / 2)
        turtle.right(60)

# Configurar la ventana y la tortuga
turtle.speed("fastest")
turtle.penup()
turtle.goto(-200, -100)
turtle.pendown()

# Ejecutar el fractal
sierpinski(400, 4)  # (Tamaño inicial, profundidad)

turtle.done()
