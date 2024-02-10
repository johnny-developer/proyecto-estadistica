# pip install scipy
from scipy.stats import norm 
from normal import normal1X, normal2X
from bernoulli import calc_bernoulli

def mostrar_menu():
    print("1. Bernoulli")
    print("2. Normal")
    print("3. Aproximacion)")
    print("4. Salir :)")

resultado = ""
    
while True:
    mostrar_menu()
    try:
        opcion = int(input("Selecciona una opción: "))
        if opcion == 1:
            #pedir datos n y p 
            resultado = calc_bernoulli (10, 1/2)
            break
        elif opcion == 2:
            while True:
                try:
                    opcion_normal = int(input("Num variables de la condicion? [1,2]: "))
                    if opcion_normal == 1:
                        #pedir datos x1, media, desviacion y pasarlos al metodo normal1X
                        resultado = normal1X(70,80,4)
                        break
                    elif opcion_normal == 2:
                        #pedir datos x1, x2, media, desviacion y pasarlos al metodo normal2X
                        resultado = normal2X(85, 90, 80, 4)
                        break
                    else:
                        print("Opción no válida.")
                except ValueError:
                    print("Error: Ingresa un número válido.")
            break
        elif opcion == 3:
            #Aproximacion
            break
        elif opcion == 4:
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida.")
    except ValueError:
        print("Error: Ingresa un número válido.")

print(resultado)
