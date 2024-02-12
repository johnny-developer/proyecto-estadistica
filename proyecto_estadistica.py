# pip install scipy
from scipy.stats import norm 
from normal import normal1X, normal2X
from bernoulli import bernoulli_uno, bernoulli_todos, bernoulli_menor_que, bernoulli_mayor_que, bernoulli_entre_2valores
from aproximacion import aprox1X, aprox2X
import os
import time


def opcion_1():
    while True:
        limpiar_consola()
        print("Has seleccionado Bernoulli")
        menu_bernouli()
        try:
            opcion_bernoulli = int(input("Eliga una opcion entre [1-5]: "))
            if opcion_bernoulli == 1:
                k = int(input("porfavor ingresa valor de x(k): "))
                n= int(input("porfavor ingrese el numero de veces(n): "))
                p = float(input("porfavor ingresa probabilidad (p):"))
                resultado = bernoulli_uno(k, n, p=1/2)
                break
            elif opcion_bernoulli == 2:
                n = int(input("ingrese el numero de veces(n): "))
                p = float(input("ingrese la probabilidad(p): "))
                resultado = bernoulli_todos(n, p)
                break
            elif opcion_bernoulli == 3:
                rango_inicio = int(input("ingrese el rango inicial: "))
                rango_fin = int(input("ingrese el rango final: "))
                n = int(input("ingrese el numero de veces(n):"))
                p = float(input("ingrese la probabilidad(p): "))
                resultado = bernoulli_entre_2valores(rango_inicio, rango_fin, n, p)
                break
            elif opcion_bernoulli == 4:
                rango_fin = int(input("ingrese el rang: "))
                n = int(input("ingrese el numero de veces(n):"))
                p = float(input("ingrese la probabilidad(p): "))
                resultado = bernoulli_menor_que(rango_fin, n, p)
                break
            elif opcion_bernoulli == 5:
                rango_inicio = int(input("ingrese el rango inicial: "))
                n = int(input("ingrese el numero de veces(n):"))
                p = float(input("ingrese la probabilidad(p): "))
                resultado = bernoulli_mayor_que(rango_inicio, n, p)
                break
            else:
                print("Opción no válida.")
                time.sleep(1)
        except ValueError:
            print("Error: Ingresa un número válido.")
            time.sleep(1)
    return resultado        

def opcion_2():
    while True:
        limpiar_consola()
        print("Has seleccionado Normal")
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
    return resultado

def opcion_3():
    while True:
        limpiar_consola()
        print("Has seleccionado aproximacion")
        try:
            opcion_normal = int(input("Num variables de la condicion? [1,2]: "))
            if opcion_normal == 1:
                x1 = int(input("ingrese el valor de x: "))
                n = int(input("ingrese el numero de veces(n): "))
                p = float(input("ingrese la probabilidad(p): "))
                resultado = aprox1X(x1, n, p)
                break
            elif opcion_normal == 2:
                x1 = int(input("ingrese el valor de x1: "))
                x2 = int(input("ingrese el valor de x2: "))
                n = int(input("ingrese el numero de veces(n): "))
                p = float(input("ingrese la probabilidad(p): "))
                resultado = aprox2X(x1, x2, n, p)
                break
            else:
                print("Opción no válida.")
                time.sleep(1)
        except ValueError:
            print("Error: Ingresa un número válido.")
            time.sleep(1)
    return resultado

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def mostrar_menu():
    limpiar_consola()
    print("\nMenú:")
    print("1. Bernoulli")
    print("2. Normal")
    print("3. Aproximacion")
    print("4. Salir")

opciones = {
    '1': opcion_1,
    '2': opcion_2,
    '3': opcion_3
}

def menu_bernouli():
    print("1. Uno")
    print("2. Todos")
    print("3. Rango")
    print("4. Menor igual que")
    print("5. Mayor igual que")
    


    
while True:
    resultado = ""
    limpiar_consola()
    mostrar_menu()
    seleccion = input("Selecciona una opción: ")

    if seleccion == '4':
        limpiar_consola()
        print("Saliendo...")
        break

    if seleccion in opciones:
        resultado = opciones[seleccion]()
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")

print(resultado)

