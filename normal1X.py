from scipy.stats import norm

media = 70
desviacion= 2

x1 = 73

px1 = norm.cdf(x1, media, desviacion)

probabilidad = px1 - 0.5000

print(f'La P(X <= {x1}) es: {probabilidad}')
