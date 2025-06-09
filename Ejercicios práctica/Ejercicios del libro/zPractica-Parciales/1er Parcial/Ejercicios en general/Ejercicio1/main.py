# Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre 
# y la cantidad de películas de la saga en la que participó, 
# implementar las funciones necesarias para resolver las siguientes actividades: 

from personajes import Personaje
from stack import Stack

personajes_stack=Stack()

personajes = [
    Personaje("Iron Man", 3),
    Personaje("Captain America", 9),
    Personaje("Black Widow", 7),
    Personaje("Rocket Raccoon", 5),
    Personaje("Groot", 5),
    Personaje("Doctor Strange", 4),
    Personaje("Gamora", 6),
    Personaje("Hawkeye", 8),
    Personaje("Captain Marvel", 3),
    Personaje("Drax", 4)
]

def CargarPila(perso_stack,personajes):
    for pj in personajes:
        perso_stack.push(pj)
        
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila; 
def determinarPersonajePos(perso_stack):
    aux_stack=Stack()
    pos=0
    encontrado=False
    
    for i in range(perso_stack.size()):
        pos+=1
        pj=perso_stack.pop()
        aux_stack.push(pj)
        
        if pj.nombre=="Rocket Raccoon" or pj.nombre=="Groot":
            encontrado=True
            print(f"La posicion donde se encuentra {pj.nombre} es: {pos}")
            
    if not encontrado:
        print("No se encontro a los personajes Rocket Raccoon y Groot.")
        
    while aux_stack.size()>0:
        perso_stack.push(aux_stack.pop())
    
    
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece; 
def determinarPersonajesParticipacion(perso_stack):
    aux_stack=Stack()
    encontrado=False
    
    while perso_stack.size()>0:
        pj=perso_stack.pop()
        aux_stack.push(pj)
        
        if pj.cantPelicula>5:
            encontrado=True
            print(f"{pj.nombre}, aparece en {pj.cantPelicula} peliculas.")
            
    if not encontrado:
        print("No se encontro personajes que participen en mas de 5 peliculas.")
        
    while aux_stack.size()>0:
        perso_stack.push(aux_stack.pop())
        
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow); 
def determinarParticipacion(perso_stack):
    aux_stack=Stack()
    encontrado=False
    
    while perso_stack.size()>0:
        pj=perso_stack.pop()
        aux_stack.push(pj)
        
        if pj.nombre=="Black Widow":
            encontrado=True
            print(f"{pj.nombre}, aparece en {pj.cantPelicula} peliculas.")
                 
    if not encontrado:
        print("No se encontro a la Viuda Negra.")
        
    while aux_stack.size()>0:
        perso_stack.push(aux_stack.pop())
        
# d. mostrar todos los personajes cuyos nombres empiezan con C, D y G.
def mostrarPersonajes(perso_stack):
    aux_stack=Stack()
    encontrado=False
    
    while perso_stack.size()>0:
        pj=perso_stack.pop()
        aux_stack.push(pj)
        
        if pj.nombre.startswith(("C", "D", "G")):
            encontrado=True
            print(f"{pj.nombre}")
                 
    if not encontrado:
        print("No se encontro personajes cuyos nombres empiezan con C, D y G")
        
    while aux_stack.size()>0:
        perso_stack.push(aux_stack.pop())
                  
#CP
CargarPila(personajes_stack,personajes)
# print("Pila de personajes cargada: ")
# personajes_stack.show()
determinarPersonajePos(personajes_stack)
print()
print("Personajes que participaron en más de 5 películas de la saga con la cantidad de películas en la que aparece: ")
determinarPersonajesParticipacion(personajes_stack)
print()
determinarParticipacion(personajes_stack)
print()
print("Personajes cuyos nombres empiezan con C, D y G: ")
mostrarPersonajes(personajes_stack)


