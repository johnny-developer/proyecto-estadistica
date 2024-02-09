from scipy.stats import norm

media = 23 
desviacion = 5 

x1 = 21
x2 = 27

px1 = norm.cdf(x1, media, desviacion)
px2 = norm.cdf(x2, media, desviacion)

probabilidad = px2 - px1

print(f'La P({x1} <= X <= {x2}) es: {probabilidad}')
