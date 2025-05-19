# 4. Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.
from list_ import List

list_numeros = List()

numeros=(21,13,45,56,32,100)

def cargarLista(list_num, numeros):
    for num in numeros:
        list_num.append(num)
        
def agregarNodo(list_num, pos, valor):
    list_num.insert(pos, valor) #este es otro tipo de cargar valores
        
#CUERPO PRINCIPAL
cargarLista(list_numeros,numeros)
print("Lista de numeros: ")
list_numeros.show()
print()
posicion=int(input("En que posicion le gustaria agregar un nuevo numero en la lista anterior?: "))
valor=int(input("Que numero quisiera ingresar?: "))
agregarNodo(list_numeros,posicion,valor)
print()
print("La lista despues de agregar el valor: ")
list_numeros.show()