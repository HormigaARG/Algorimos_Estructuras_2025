# 16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
# strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
# permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
# bos episodios.

from stack import Stack
personajes_stack1 = Stack()
personajes_stack2 = Stack()
interseccion_stack = Stack()

personajesV = ["Luke Skywalker", "Darth Vader", "Leia Organa", "Yoda"]
personajesVII = ["Rey", "Poe Dameron", "Kylo Ren", "Han Solo"]

def cargarPila1(perso_stack1,personajesV):
    for pj in personajesV:
        perso_stack1.push(pj)
        
def cargarPila2(perso_stack2,personajesVII):
    for pj in personajesVII:
        perso_stack2.push(pj)
        
def interseccionPilas(perso_stack1,perso_stack2,inter_stack):
    aux_stack1=Stack()
    aux_stack2=Stack()
    while perso_stack1.size()>0:
        elemento1=perso_stack1.pop()
        aux_stack1.push(elemento1)
    
    while perso_stack2.size()>0:
        elemento2=perso_stack2.pop()
        aux_stack2.push(elemento2)
    
    while aux_stack1.size()>0:
        aux_stack2.push(aux_stack1.pop())
        
    while aux_stack2.size()>0:
        inter_stack.push(aux_stack2.pop())

cargarPila1(personajes_stack1,personajesV)
cargarPila2(personajes_stack2,personajesVII)
print("Pila de personajes episodio V: ")
personajes_stack1.show()
print()
print("Pila de personajes episodio VII: ")
personajes_stack2.show()
print()
interseccionPilas(personajes_stack1,personajes_stack2,interseccion_stack)
print("Pila de interseccion de ambas pilas: ")
interseccion_stack.show()