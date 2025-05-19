# 7. Implementar los algoritmos necesarios para resolver las siguientes tareas:
# a. concatenar dos listas, una atrás de la otra;
# b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
# c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
# d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.

from list_ import List

list_numeros1 = List()
list_numeros2 = List()
list_final = List()

numeros1=(21,13,45,56,32,100)
numeros2=(21,45,100,33,24,11)

def cargarLista(list_num, numeros):
    for num in numeros:
        list_num.append(num)
        

#a     
def concatenarListas(list_num1,list_num2):
    aux_list= List()
    for num in list_num1:
        aux_list.append(num)
    
    for num2 in list_num2:
        aux_list.append(num2)
    
    return aux_list
 
#b       
def concatenarListasOmitiendo(list_num1, list_num2, list_finish):
    ya_agregados = List()
    for num in list_num1:
        if num not in ya_agregados:
            ya_agregados.append(num)
            list_finish.append(num)
            
    for num in list_num2:
        if num not in ya_agregados:
            ya_agregados.append(num)
            list_finish.append(num)
    
#c
def contarElementosRepetidos(list_num1, list_num2):
    repetidos = List()
    for num1 in list_num1:
        for num2 in list_num2:
            if num1 == num2 and num1 not in repetidos:
                repetidos.append(num1)
    return len(repetidos)

#d
def eliminarNodos(lista):
    while len(lista) > 0:
        valor = lista[0]  # siempre eliminamos el primer elemento
        eliminado = lista.delete_value(valor)
        print(f"Nodo eliminado: {eliminado}")

    
#CUERPO PRINCIPAL
cargarLista(list_numeros1, numeros1)
cargarLista(list_numeros2, numeros2)
print("Lista concatenada: ")
aux_list_final=concatenarListas(list_numeros1,list_numeros2)
aux_list_final.show()
print()
print("Lista concatenada en una sola omitiendo los datos repetidos y manteniendo su orden: ")
concatenarListasOmitiendo(list_numeros1,list_numeros2,list_final)
list_final.show()
contadorElementos=contarElementosRepetidos(list_numeros1,list_numeros2)
print(f"La cantidad de elementos repetidos hay entre dos listas es de: {contadorElementos}")
print()
print("Elimino los nodos, por ejemplo de la LISTA 1: ")
eliminarNodos(list_numeros1)

