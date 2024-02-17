import turtle

# Función para dibujar una palabra con un color específico
def dibujar_palabra_con_color(palabra, color_palabra, color_fondo):
    # Configuración inicial de la ventana
    ventana = turtle.Screen()
    ventana.bgcolor(color_fondo)  # Establecer color de fondo

    # Configuración inicial de la tortuga
    t = turtle.Turtle()
    t.speed(0)  # Configura la velocidad de dibujo más rápida

    # Configuración del color de la palabra
    t.color(color_palabra)

    # Dibuja la palabra en la pantalla
    t.write(palabra, align='center', font=('Arial', 24, 'normal'))

    # Oculta la tortuga y finaliza
    t.hideturtle()
    ventana.mainloop()

# Llamada a la función para dibujar la palabra "marrón" con fondo marrón
dibujar_palabra_con_color("Marrón", "brown", "white")
