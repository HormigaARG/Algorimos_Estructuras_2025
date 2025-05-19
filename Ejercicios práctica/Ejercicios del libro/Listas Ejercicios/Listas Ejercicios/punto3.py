#3. Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos,
#una que contenga los números pares y otra para los números impares.

from list_ import List

list_numeros = List()
list_pares = List()
list_impares = List()

numeros=(21,13,45,56,32,100)

def cargarLista(list_num, numeros):
    for num in numeros:
        list_num.append(num)
        
def dividirLista(list_num, list_par, list_impar):
    for num in list_num:
        if num % 2 == 0:
            list_par.append(num)
        else:
            list_impar.append(num)
        
        
#CUERPO PRINCIPAL
cargarLista(list_numeros,numeros)
print("Lista de numeros: ")
list_numeros.show()
dividirLista(list_numeros,list_pares,list_impares)
print()
print("Lista con numeros pares: ")
list_pares.show()
print()
print("Lista con numeros impares: ")
list_impares.show()


