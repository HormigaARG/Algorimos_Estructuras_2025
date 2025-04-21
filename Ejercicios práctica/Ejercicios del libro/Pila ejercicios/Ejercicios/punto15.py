#15. Realizar el algoritmo de ordenamiento quicksort de manera que funcione iterativamente.

from stack import Stack
number_stack= Stack()

numbers= [30, 10, 50, 40, 20]
def cargarPila(num_stack,numbers):
    for number in numbers:
        num_stack.push(number)
        
def quickSort(num_stack):
    pivote=num_stack.pop()
    
    
    
cargarPila(number_stack,numbers)
print("Pila original: ")
number_stack.show()