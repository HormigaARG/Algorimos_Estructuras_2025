#4. Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.
from queue import Queue
from random import randint

number_queue= Queue()

def cargarCola(num_queue):
    for i in range(5):
        num_queue.arrive(randint(1,10))
        
cargarCola(number_queue)
print("La cola original: ")
number_queue.show()
        