# 8.Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un mazo de
#   cartas de baraja española,resolver las siguientes actividades:
# a. generar las cartas del mazo de forma aleatoria;
# b. separar la pila mazo en cuatro pilas una por cada palo;
# c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.

from random import randint, choice
from stack import Stack

mazo_stack = Stack()
espada_stack = Stack()
basto_stack = Stack()
copa_stack = Stack()
oro_stack = Stack()

palos = ["espada", "basto", "copa", "oro"]

#a)
def cargar_mazo(maz_stack):
    for i in range(10): 
        numero = randint(1, 12)
        palo = choice(palos)
        carta = f"{numero} de {palo}"
        maz_stack.push(carta)

#b)
def separar_pilas(maz_stack, esp_stack, bas_stack, cop_stack, or_stack):
    while maz_stack.size() > 0:
        carta = maz_stack.pop()
        if "espada" in carta: #esto es otra forma de verificar si es que contiene el palo en la carta
            esp_stack.push(carta)
        elif "basto" in carta:
            bas_stack.push(carta)
        elif "copa" in carta:
            cop_stack.push(carta)
        elif "oro" in carta:
            or_stack.push(carta)
    
    
#c)
def ordenar_pila_creciente(esp_stack):
    lista = []
    while esp_stack.size() >0 :
        carta = esp_stack.pop()
        numero = int(carta.split(" de ")[0]) #esto es para que me guarde unicamente el numero y me quite el "de"
        lista.append((numero, carta)) #agrega los numeros y el palo

    # Ordenar por número
    lista.sort()

    # Volver a cargar en la pila (orden creciente)
    for (numero, carta) in reversed(lista):
        esp_stack.push(carta)

# Mostrar una pila con título
def mostrar_pila(nombre, palo):
    print(f"{nombre}:")
    palo.show()
    print()

# Ejecutar
cargar_mazo(mazo_stack)
print("Pila original (mazo aleatorio):")
mazo_stack.show()
print()

separar_pilas(mazo_stack, espada_stack, basto_stack, copa_stack, oro_stack)

# Mostrar pilas separadas
mostrar_pila("Pila de espada", espada_stack)
mostrar_pila("Pila de basto", basto_stack)
mostrar_pila("Pila de copa", copa_stack)
mostrar_pila("Pila de oro", oro_stack)

# Ordenar por ejemplo la pila de espada
ordenar_pila_creciente(espada_stack)
print("Pila de espada ordenada (creciente):")
espada_stack.show()
