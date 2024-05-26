
from LinearCongruentialGenerator import LinearCongruentialGenerator

class Environment:
    def __init__(self, seed):
        self.rng = LinearCongruentialGenerator(seed)  # Inicializar el LCG con la semilla

    def generate_observation_vector(self):
        carbohydrates = round(self.rng.next() / 1000000000.0, 1)  # Normalizar y ajustar rango si es necesario
        temperature = self.rng.next() % 42 + 4  # Ajustar rango a [4, 45]
        competence = self.rng.next() % 1001  # Ajustar rango a [0, 1000]
        ph = self.rng.next() % 10  # Ajustar rango a [0, 9]

        return [carbohydrates, temperature, competence, ph]



