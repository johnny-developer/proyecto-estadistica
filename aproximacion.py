import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

def Aprox(n,p):
    # Generar datos de la distribución binomial
    binomial_calculo = np.random.binomial(n, p, 1000)

    # Calcular la media y la desviación estándar de la distribución binomial
    media_binomial = np.mean(binomial_calculo)
    desviacion_binomial = np.std(binomial_calculo)

    # Aproximación a la distribución normal usando el teorema del límite central
    normal_approximacion = norm(loc=media_binomial, scale=desviacion_binomial)

    # Generar datos para la distribución normal aproximada
    x = np.linspace(min(binomial_calculo), max(binomial_calculo), 100)
    pdf_normal_approximacion = normal_approximacion.pdf(x)

    # Graficar los resultados
    plt.hist(binomial_calculo, bins=20, density=True, alpha=0.5, label='Distribución Binomial')
    plt.plot(x, pdf_normal_approximacion, color='red', label='Aproximación Normal')
    plt.title('Aproximación Binomial a Normal')
    plt.xlabel('Valor')
    plt.ylabel('Densidad de Probabilidad')
    plt.legend()
    return 'ejemplo exitoso'