import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from reportlab.pdfgen import canvas

# Ejemplo 1
data = {'ganancia': [20, 25, 34, 30, 33, 34, 36, 35, 40, 37, 41, 20],
        'inversion': [2, 4, 5, 4, 6, 5, 5, 7, 8, 7, 8, 2]}

ejemplo1 = pd.DataFrame(data)

# Paso 2: Diagrama de dispersión
plt.scatter(ejemplo1['inversion'], ejemplo1['ganancia'])
plt.xlabel('Inversión')
plt.ylabel('Ganancia')
plt.title('Diagrama de dispersión')
plt.savefig('scatter_plot.png')
plt.close()

# Paso 3: Coeficiente de correlación
correlacion = ejemplo1.corr().iloc[0, 1]

# Paso 4: Regresión lineal simple
X = sm.add_constant(ejemplo1['inversion'])  # Añadir una columna de unos para el intercepto
modelo = sm.OLS(ejemplo1['ganancia'], X).fit()

# Crear documento PDF
with canvas.Canvas("reporte.pdf") as pdf:
    pdf.drawString(100, 800, "Modelos Predictivos")
    pdf.drawString(100, 780, "Autor: Abraham")
    pdf.drawString(100, 760, f"Fecha: {pd.to_datetime('today').strftime('%Y-%m-%d')}")

    # Agregar información sobre el ejemplo
    pdf.drawString(100, 740, "Ejemplo 1:")
    pdf.drawString(100, 720, str(ejemplo1))

    # Agregar el diagrama de dispersión
    pdf.drawInlineImage('scatter_plot.png', 100, 600)

    # Agregar información sobre la correlación
    pdf.drawString(100, 500, f"Coeficiente de correlación: {correlacion}")

    # Agregar información sobre la regresión lineal
    pdf.drawString(100, 480, "Regresión Lineal:")
    pdf.drawString(100, 460, str(modelo.summary()))

    # Agregar información adicional si es necesario

print("Documento PDF creado exitosamente.")
