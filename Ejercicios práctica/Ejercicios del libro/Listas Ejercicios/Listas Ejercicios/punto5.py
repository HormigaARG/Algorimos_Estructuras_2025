# 5. Dada una lista de números enteros eliminar de estas los números primos.
from list_ import List

list_numeros = List()

numeros=(2,3,45,7,32,5)

def cargarLista(list_num, numeros):
    for num in numeros:
        list_num.append(num)
        
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def eliminarPrimos(list_num):
    for num in list(list_num): #se puede crear una copia temporal con list(list_num) asi no tengo problema cuando itero.
        if es_primo(num)==True:
            list_num.delete_value(num)
        
        
#CUERPO PRINCIPAL
cargarLista(list_numeros,numeros)
print("Lista de numeros: ")
list_numeros.show()
print()
eliminarPrimos(list_numeros)
print("Lista sin numeros primos: ")
list_numeros.show()