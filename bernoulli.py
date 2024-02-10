from scipy.special import comb



def calc_bernoulli (k, n, p, q):
    
    combinacion = comb(n, k)
    exito = p ** k
    fracaso = q ** (n-k)
    resultado = combinacion * exito * fracaso
    return f'Bernoulli: {resultado}' 