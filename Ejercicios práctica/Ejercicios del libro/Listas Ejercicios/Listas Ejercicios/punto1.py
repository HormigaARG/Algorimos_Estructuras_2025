#1. Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.
from list_ import List

list_numeros = List()

def cargarLista(list_num):
    op = input("¿Desea cargar un número a la lista? (S/N): ")
    while op.lower() == "s":
        number = int(input("Número a cargar: "))
        list_num.append(number)
        op = input("¿Desea cargar un nuevo número a la lista? S/N ")

def contadorNodos(list_num):
    contador=0
    for i in list_num:
        contador+=1
    return contador
        
               
#CUERPO PRINCIPAL
cargarLista(list_numeros)
print()
print("Lista cargada de numeros: ")
list_numeros.show()
print()
contador_nodos=contadorNodos(list_numeros)
print(f"La cantidad de nodos que tiene la lista es de: {contador_nodos}")