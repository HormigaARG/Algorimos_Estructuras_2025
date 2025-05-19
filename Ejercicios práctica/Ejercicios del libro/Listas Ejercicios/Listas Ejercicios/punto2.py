#2. Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.
from list_ import List

list_caracteres = List()

caracteres = ('a', 'b', 'e', 'f', 'i', 'o', 'u', 'x', 'z')

def cargarLista(list_car,caracteres):
    for char in caracteres:
        list_car.append(char)
        

def eliminarVocales(list_carac):
    vocales = "aeiou"
    for vocal in vocales: #para cada vocal verifico si esta en la lista, y si llega a estar la elimina de la misma
        while vocal in list_carac:
            list_carac.delete_value(vocal)
        
#CUERPO PRINCIPAL
cargarLista(list_caracteres,caracteres)
print()
print("Lista cargada de caracteres: ")
list_caracteres.show()
print()
eliminarVocales(list_caracteres)
print("Lista eliminando a todas las vocales: ")
list_caracteres.show()