import os;

def opcion_1():
    while True:
        limpiar_consola()
        print("Has seleccionado Bernoulli")
        respuesta = input("¿Deseas realizar una nueva operacion? (s/n): ")
        if respuesta.lower() != 's':
            break

def opcion_2():
    while True:
        limpiar_consola()
        print("Has seleccionado normal")
        respuesta = input("¿Deseas realizar una nueva operacion? (s/n): ")
        if respuesta.lower() != 's':
            break

def opcion_3():
    while True:
        limpiar_consola()
        print("Has seleccionado aproximacion")
        respuesta = input("¿Deseas realizar una nueva operacion? (s/n): ")
        if respuesta.lower() != 's':
            break

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

while True:
    mostrar_menu()
    seleccion = input("Selecciona una opción: ")

    if seleccion == '4':
        limpiar_consola()
        print("Saliendo...")
        break

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")
