# pip install scipy
from scipy.stats import norm 
from normal import normal1X, normal2X
from bernoulli import bernoulli_todos, bernoulli_entre_2valores, bernoulli_menor_que, bernoulli_mayor_que, bernoulli_uno
from aproximacion import aprox1X, aprox2X
import os
import time

# Función para limpiar la consola
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("1. -----Bernoulli------")
    print("2. ------Normal--------")
    print("3. ---Aproximacion-----")
    print("4. Salir")

def menu_bernouli():
    print("1. Uno")
    print("2. Todos")
    print("3. Rango")
    print("4. Menor que")
    print("5. Mayor que")
    

resultado = ""
    
while True:
    limpiar_consola()
    mostrar_menu()
    try:
        opcion = int(input("Selecciona una opción: "))
        if opcion == 1:
            while True:
                limpiar_consola()
                print("===========BERNOULLI============")
                menu_bernouli()
                try:
                    opcion_bernoulli = int(input("Eliga una opcion entre [1-5]: "))
                    if opcion_bernoulli == 1:
                        k = float(input("porfavor ingresa valor de x(k): "))
                        n= float(input("porfavor ingrese el numero de veces(n): "))
                        p = float(input("porfavor ingresa probabilidad (p):"))
                        resultado = bernoulli_uno(k, n, p=1/2)
                        break
                    elif opcion_bernoulli == 2:
                        n = float(input("ingrese el numero de veces(n): "))
                        p = float(input("ingrese la probabilidad(p): "))
                        resultado = bernoulli_todos(n, p)
                        break
                    elif opcion_bernoulli == 3:
                        rango_inicio = float(input("ingrese el rango inicial: "))
                        rango_fin = float(input("ingrese el rango final: "))
                        n = float(input("ingrese el numero de veces(n):"))
                        p = float(input("ingrese la probabilidad(p): "))
                        resultado = bernoulli_entre_2valores(rango_inicio, rango_fin, n, p)
                        break
                    elif opcion_bernoulli == 4:
                        rango_fin = float(input("ingrese el rang: "))
                        n = float(input("ingrese el numero de veces(n):"))
                        p = float(input("ingrese la probabilidad(p): "))
                        resultado = bernoulli_menor_que(rango_fin, n, p)
                        break
                    elif opcion_bernoulli == 5:
                        rango_inicio = float(input("ingrese el rango inicial: "))
                        n = float(input("ingrese el numero de veces(n):"))
                        p = float(input("ingrese la probabilidad(p): "))
                        resultado = bernoulli_mayor_que(rango_inicio, n, p)
                        break
                    else:
                        print("Opción no válida.")
                        time.sleep(1)
                except ValueError:
                    print("Error: Ingresa un número válido.")
                    time.sleep(1)
            break
        elif opcion == 2:
            while True:
                limpiar_consola()
                print("===========NORMAL============")
                try:
                    opcion_normal = int(input("Num variables de la condicion? [1-2]: "))
                    if opcion_normal == 1:
                        x1 = float(input("ingrese el valor de x: "))
                        media = float(input("ingrese la media: "))
                        desviacion = float(input("ingrese la desviacion: "))
                        resultado = normal1X(x1, media, desviacion)
                        break
                    elif opcion_normal == 2:
                        x1 = float(input("ingrese el valor de x1: "))
                        x2 = float(input("ingrese el valor de x2: "))
                        media = float(input("ingrese la media: "))
                        desviacion = float(input("ingrese la desviacion: "))
                        resultado = normal2X(x1, x2, media, desviacion)
                        break
                    else:
                        print("Opción no válida.")
                        time.sleep(1)
                except ValueError:
                    print("Error: Ingresa un número válido.")
                    time.sleep(1)
            break
        elif opcion == 3:
            while True:
                limpiar_consola()
                print("===========APROXIMACION============")
                try:
                    opcion_normal = int(input("Num variables de la condicion? [1,2]: "))
                    if opcion_normal == 1:
                        x1 = float(input("ingrese el valor de x: "))
                        n = float(input("ingrese el numero de veces(n): "))
                        p = float(input("ingrese la probabilidad(p): "))
                        resultado = aprox1X(x1, n, p)
                        break
                    elif opcion_normal == 2:
                        x1 = float(input("ingrese el valor de x1: "))
                        x2 = float(input("ingrese el valor de x2: "))
                        n = float(input("ingrese el numero de veces(n): "))
                        p = float(input("ingrese la probabilidad(p): "))
                        resultado = aprox2X(x1, x2, n, p)
                        break
                    else:
                        print("Opción no válida.")
                        time.sleep(1)
                except ValueError:
                    print("Error: Ingresa un número válido.")
                    time.sleep(1)
            break
        elif opcion == 4:
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida.")
            time.sleep(1)
    except ValueError:
        print("Error: Ingresa un número válido.")
        time.sleep(1)

print(resultado)
print()
