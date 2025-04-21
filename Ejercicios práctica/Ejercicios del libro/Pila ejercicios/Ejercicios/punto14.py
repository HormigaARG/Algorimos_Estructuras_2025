# 14. Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden orde-
# nados de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra –no se
# pueden utilizar métodos de ordenamiento–.
from random import randint
from stack import Stack

number_stack = Stack()

def cargarPila(num_stack):
    for i in range(5):
        rand_number = randint(1, 100)
        num_stack.push(rand_number)

def ordenarPilaCreciente(num_stack):
    aux_stack = Stack()
    
    while num_stack.size() > 0:
        elemento = num_stack.pop()
        
        
        while aux_stack.size()>0 and aux_stack.on_top()>elemento:
            num_stack.push(aux_stack.pop())
            
        aux_stack.push(elemento)
        
                  
            
    
    while aux_stack.size() > 0:
        num_stack.push(aux_stack.pop())

# Uso
cargarPila(number_stack)
print("Pila original:")
number_stack.show()

ordenarPilaCreciente(number_stack)
print("Pila ordenada de forma creciente (de abajo hacia arriba):")
number_stack.show()

