def calcular_probabilidad_bernuolli(p, n, k):
    q = 1 - p
    
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    def combinacion(n, k):
        return factorial(n) / (factorial(k) * factorial(n - k))

    def bernoulli(p, q, n, k):
        return combinacion(n, k) * (p ** k) * (q ** (n - k))

    if p < 0 or p > 1:
        print("La probabilidad debe estar en el rango [0, 1].")
        return None
    
    if k < 0 or k > n:
        print("El número de éxitos debe estar en el rango [0, n].")
        return None
    
    probability = bernoulli(p, q, n, k)
    
    return probability