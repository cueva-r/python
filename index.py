import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x)
def f(x):
    return x + 5

# Definir la función g(x)
def g(x):
    return x - 3

# Definir la función f(x) + g(x)
def f_plus_g(x):
    return f(x) + g(x)

# Crear un rango de valores de x
x = np.linspace(-10, 10, 400)

# Calcular los valores de y para f(x), g(x) y f(x) + g(x)
y_f = f(x)
y_g = g(x)
y_f_plus_g = f_plus_g(x)

# Graficar f(x), g(x) y f(x) + g(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y_f, label='f(x) = x + 5', color='blue')
plt.plot(x, y_g, label='g(x) = x - 3', color='red')
plt.plot(x, y_f_plus_g, label='f(x) + g(x) = 2x + 2', linestyle='--', color='green')

# Etiquetas y título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de f(x) = x + 5, g(x) = x - 3 y f(x) + g(x) = 2x + 2')

# Agregar la leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()
