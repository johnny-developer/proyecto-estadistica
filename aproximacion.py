from scipy.special import comb

def calc_bernoulli (n, p):
    q = 1 - p
    sum = 0
    for i in range(n+1):
        combinacion = comb(n, i)
        exito = p ** i
        fracaso = q ** (n-i)
        resultado = combinacion * exito * fracaso
        sum = sum + resultado
        print(f'P({i}): {resultado}')
        
    return f'Bernoulli sumatoria: {sum}'