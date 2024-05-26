import matplotlib.pyplot as plt
import numpy as np

from Enviroment.Carbohydrate import carbohydrate_adjust
from Enviroment.Competence import competence_adjust
from Enviroment.Enviroment import Environment  # Importar la clase Environment
from Enviroment.PH import ph_adjust
from Enviroment.Temperatura import temperature_adjust
from agent.Bacterium import gompertz_function

valuek = 0.5
valuer = -0.01
values = []
iterations = list(range(1, 501))
counter = 0

gompertz_values = []

env = Environment(seed=1234)  # Crear una instancia de Environment con la semilla deseada

for _ in iterations:
    values = env.generate_observation_vector()  # Usar el método de la clase Environment
    modifications = [
        carbohydrate_adjust(values[0]),
        temperature_adjust(values[1]),
        competence_adjust(values[2]),
        ph_adjust(values[3])
    ]

    kmodification = modifications[0] + modifications[1]
    rmodification = modifications[3] + modifications[2]

    i = gompertz_function(
        5,
        100,
        valuer + rmodification,
        valuek + kmodification,
        2
    )
    print(f"En el tiempo {counter} el cambio para k fue {kmodification} y para r fue {rmodification}")
    counter += 1
    gompertz_values.append(i)

def gompertz_growth(t, A, B, C):
    """
    Función de Gompertz para modelar el crecimiento.

    Parámetros:
        t (array): Array de tiempo.
        A (float): Parámetro de escala.
        B (float): Parámetro de velocidad.
        C (float): Parámetro de asintota.

    Devuelve:
        Array de crecimiento según la función de Gompertz.
    """
    return A * np.exp(-np.exp(B - C * t))

# Generar datos de tiempo
t = np.linspace(0, 500, 100)

# Parámetros de la función de Gompertz
A = 600.0  # Parámetro de escala
B = 0.03  # Parámetro de velocidad
C = 0.01  # Parámetro de asintota

# Calcular el crecimiento según la función de Gompertz
growth = gompertz_growth(t, A, B, C)

# Graficar
plt.figure(figsize=(8, 6))
plt.plot(t, growth, label='Función de Gompertz')
plt.title('Crecimiento según la función de Gompertz')
plt.xlabel('Tiempo')
plt.ylabel('Numero de bacterias')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(iterations, gompertz_values)
plt.xlabel('Tiempo')
plt.ylabel('Numero de bacterias')
plt.title('Población')
plt.show()






