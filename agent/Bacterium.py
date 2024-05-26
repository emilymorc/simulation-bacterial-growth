import numpy as np

def gompertz_function(t, N0, r, k, tl):
    # Verificar las condiciones para k y r
    if not (0 <= k <= 1):
        k = 0.5
    if not (-1 <= r <= 1):
        r = -0.03

    # Calcular el exponente basado en los parámetros permitidos
    exponent = -np.exp(-k * (t - tl)) * r * (t - tl)
    N_t = N0 * np.exp(exponent)
    return N_t
