from scipy.stats import norm
     
def normal2X(x1, x2, media, desviacion):
    while True:
        opcion = input("Ambos incluidos? y/n: ")
        if opcion == 'y':
            break
        elif opcion == "n":
            x1 = x1 - 1
            x2 = x2 - 1
            break
        else:
            print("Opción no válida.")
            continue
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
    return f'La P({x1} <= X <= {x2}) es: {probabilidad}'





def menu():
    print("Eliga la opcion")
    print("1. P(Z <= x1)")
    print("2. P(Z >= x1)")
        
def normal1X(x1, media, desviacion):
    while True:
        opcion = input("Ambos incluidos? y/n: ")
        if opcion == 'y':
            break
        elif opcion == "n":
            x1 = x1 - 1
            break
        else:
            print("Opción no válida.")
            continue  
    while True:
        menu()
        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion == 1:
                cadena= 'P(X <= {x1})'
                z1 =  norm.cdf(x1, media, desviacion)
            elif opcion == 2:
                cadena= 'P(X >= {x1})'
                z1 =  1 - norm.cdf(x1, media, desviacion)
            else:
                print("Opción no válida.")
                continue
        except ValueError:
            print("Error: Ingresa un número válido.")
    return f'La {cadena} es: {z1}'
