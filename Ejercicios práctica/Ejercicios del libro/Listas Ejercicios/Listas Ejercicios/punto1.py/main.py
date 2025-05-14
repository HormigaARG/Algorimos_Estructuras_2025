#1. Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.
from list_ import List
from persona import Persona

list_people = List()

people = [
    Persona("Axel"),
    Persona("Mauro"),
    Persona("Sebastian"),
    Persona("Lucas"),
    Persona("Graciela"),
]


def cargarLista(list_peo,people):
    for person in people:
        list_peo.append(person)

def contadorNodos(list_peo):
    contador=0
    for i in list_peo:
        contador+=1
        
    return contador
        
               
#CUERPO PRINCIPAL
cargarLista(list_people,people)
print("Lista cargada: ")
list_people.show()
print()
contador_nodos=contadorNodos(list_people)
print(f"La cantidad de nodos que tiene la lista es de: {contador_nodos}")