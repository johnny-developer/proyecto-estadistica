from scipy.special import comb


def bernoulli_uno(k, n, p):
    q = 1 - p
    combinacion = comb(n, k)
    exito = p ** k
    fracaso = q ** (n-k)
    resultado = combinacion * exito * fracaso
    return f'P({k}): {resultado}'

def bernoulli_todos (n, p):
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


def bernoulli_entre_2valores(rango_inicio, rango_fin, n, p):
    q = 1 - p
    sum = 0
    for i in range(rango_inicio, rango_fin + 1):
        combinacion = comb(n, i)
        exito = p ** i
        fracaso = q ** (n-i)
        resultado = combinacion * exito * fracaso
        sum = sum + resultado
        print(f'P({i}): {resultado}')
    return f'Bernoulli sumatoria: {sum}'


def bernoulli_menor_que(rango_fin, n, p):
    q = 1 - p
    sum = 0
    for i in range(0, rango_fin + 1):
        combinacion = comb(n, i)
        exito = p ** i
        fracaso = q ** (n-i)
        resultado = combinacion * exito * fracaso
        sum = sum + resultado
        print(f'P({i}): {resultado}')
    return f'Bernoulli sumatoria: {sum}'


def bernoulli_mayor_que(rango_inicio, n, p):
    q = 1 - p
    sum = 0
    for i in range(rango_inicio, n + 1):
        combinacion = comb(n, i)
        exito = p ** i
        fracaso = q ** (n-i)
        resultado = combinacion * exito * fracaso
        sum = sum + resultado
        print(f'P({i}): {resultado}')
    return f'Bernoulli sumatoria: {sum}'