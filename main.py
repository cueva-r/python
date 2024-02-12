import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Ejemplo 1
data = {'ganancia': [20, 25, 34, 30, 33, 34, 36, 35, 40, 37, 41, 20],
        'inversion': [2, 4, 5, 4, 6, 5, 5, 7, 8, 7, 8, 2]}

ejemplo1 = pd.DataFrame(data)
print(ejemplo1)

# Paso 2: Diagrama de dispersión
plt.scatter(ejemplo1['inversion'], ejemplo1['ganancia'])
plt.xlabel('Inversión')
plt.ylabel('Ganancia')
plt.title('Diagrama de dispersión')
plt.show()

# Paso 3: Coeficiente de correlación
correlacion = ejemplo1.corr().iloc[0, 1]
print(f"Coeficiente de correlación: {correlacion}")

# Paso 4: Regresión lineal simple
X = sm.add_constant(ejemplo1['inversion'])  # Añadir una columna de unos para el intercepto
modelo = sm.OLS(ejemplo1['ganancia'], X).fit()

# Resumen de resultados
print(modelo.summary())

# Predicción de nuevos valores
nueva_inversion = 10
prediccion_ganancia = modelo.predict([1, nueva_inversion])
print(f"Predicción de ganancia para una inversión de {nueva_inversion}: {prediccion_ganancia[0]}")
