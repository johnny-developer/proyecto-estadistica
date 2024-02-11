
from scipy.stats import norm
from math import sqrt
from bernoulli import bernoulli_entre_2valores, bernoulli_menor_que, bernoulli_mayor_que

def aprox2X(x1, x2, n, p):
    q = 1 -p
    media = n * p
    desviacion = sqrt((n * p * q))
    bernoulli = bernoulli_entre_2valores(x1, x2, n, p)
    x1 = x1 - 0.5    
    x2 = x2 + 0.5
    z1 = norm.cdf(x1, media, desviacion)
    z2 = norm.cdf(x2, media, desviacion)  
    if z1 <= 0 <= z2:
       probabilidad = z2 + z1
    elif z1 <= z2 <= 0:
       probabilidad = z1 - z2
    elif 0 <= z1 <= z2:
       probabilidad = z2 - z1 
    else:
        return 'Ocurrio un error'
    print("")
    return f'P({x1} <= X <= {x2}): {probabilidad} \n{bernoulli}'


def menu():
    print("Eliga la opcion")
    print("1. P(Z <= x1)")
    print("2. P(Z >= x1)")
        
def aprox1X(x1, n, p):
    q = 1 -p
    media = n * p
    desviacion = sqrt((n * p * q))
    while True:
        menu()
        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion == 1:
                cadena = f'P(X <= {x1})'
                bernoulli = bernoulli_menor_que(x1, n, p)
                x1 = x1 + 0.5    
                z1 =  norm.cdf(x1, media, desviacion)
                break
            elif opcion == 2:
                cadena = f'P(X >= {x1})'
                bernoulli = bernoulli_mayor_que(x1, n, p)
                x1 = x1 - 0.5    
                z1 = 1 - norm.cdf(x1, media, desviacion)
                break
            else:
                print("Opción no válida.")
                continue
        except ValueError:
            print("Error: Ingresa un número válido.")
    print("")
    return f'{cadena}: {z1} \n{bernoulli}'

