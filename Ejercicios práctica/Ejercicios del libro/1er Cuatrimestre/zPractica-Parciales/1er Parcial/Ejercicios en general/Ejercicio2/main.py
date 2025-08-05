# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), 
# de los cuales se conoce el nombre del personaje,
# el nombre del superhéroe y su género (Masculino M y Femenino F)  
#–por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M},
# {Natasha Ro-manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades: 

from personaje import Personaje
from queue import Queue

personajes_queue=Queue()



personajes=[
    Personaje("Tony Stark", "Iron Man", "M"),
    Personaje("Steve Rogers", "Capitán América", "M"),
    Personaje("Natasha Romanoff", "Black Widow", "F"),
    Personaje("Carol Danvers", "Capitana Marvel", "F"),
    Personaje("Scott Lang", "Ant-Man", "M"),
]

def cargarCola(perso_queue,personajes):
    for pj in personajes:
        perso_queue.arrive(pj)
        
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;  
def determinarNombrePJ(perso_queue):
    encontrado=False
    
    for i in range(perso_queue.size()):
        pj=perso_queue.on_front()
        
        if pj.nombreSH=="Capitana Marvel":
            encontrado=True
            print(f"{pj.nombrePJ}")
        
        perso_queue.move_to_end()
        
    if not encontrado:
        print("No se encontro a la super Heroe Capitana Marvel.")

# b. mostrar los nombres de los superhéroes femeninos;  
def mostrarNombreSHF(perso_queue):
    encontrado=False
    
    for i in range(perso_queue.size()):
        pj=perso_queue.on_front()

        if pj.genero=="F":
            encontrado=True
            print(f"{pj.nombreSH}")
        
        perso_queue.move_to_end()
        
    if not encontrado:
        print("No se encontro superheroes femeninos.")
        
# c. mostrar los nombres de los personajes masculinos;
def mostrarNombrePJM(perso_queue):
    encontrado=False
    
    for i in range(perso_queue.size()):
        pj=perso_queue.on_front()

        if pj.genero=="M":
            encontrado=True
            print(f"{pj.nombrePJ}")
        
        perso_queue.move_to_end()
        
    if not encontrado:
        print("No se encontro personajes masculinos.")
    
# d. determinar el nombre del superhéroe del personaje Scott Lang;  
def determinarNombreSHEspecifico(perso_queue):
    encontrado=False
    
    for i in range(perso_queue.size()):
        pj=perso_queue.on_front()

        if pj.nombrePJ=="Scott Lang":
            encontrado=True
            print(f"{pj.nombreSH}")
        
        perso_queue.move_to_end()
        
    if not encontrado:
        print("No se encontro al personaje Scott Lang.")
        

# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;  
def mostrarDatosSHyPJ(perso_queue):
    encontrado=False
    
    for i in range(perso_queue.size()):
        pj=perso_queue.on_front()

        if pj.nombrePJ[0]=="S" or pj.nombreSH[0]=="S":
            encontrado=True
            print(f"{pj}")
        
        perso_queue.move_to_end()
        
    if not encontrado:
        print("No se encontro superhéroes o personaje cuyos nombres comienzan con la letra S.")
        
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes. 
def determinarPJexistente(perso_queue):
    encontrado=False
    
    for i in range(perso_queue.size()):
        pj=perso_queue.on_front()

        if pj.nombrePJ=="Carol Danvers":
            encontrado=True
            print(f"Si, el nombre de su super heroe es: {pj.nombreSH}")
        
        perso_queue.move_to_end()
        
    if not encontrado:
        print("No, el personaje Carol Danvers no se encuentra en la cola.")
    
    
    
        
#CP
cargarCola(personajes_queue,personajes)
# personajes_queue.show()
print()
print("Nombre del personaje de la superhéroe Capitana Marvel: ")
determinarNombrePJ(personajes_queue)
print()
print()
print("Nombres de los superhéroes femeninos: ")
mostrarNombreSHF(personajes_queue)
print()
print("Nombres de los personajes masculinos: ")
mostrarNombrePJM(personajes_queue)
print()
print("Nombre del superhéroe del personaje Scott Lang: ")
determinarNombreSHEspecifico(personajes_queue)
print()
print("Todos los datos de superhéroes o personaje cuyos nombres comienzan con la letra S: ")
mostrarDatosSHyPJ(personajes_queue)
print()
print("¿El personaje Carol Danvers se encuentra en la cola?: ")
determinarPJexistente(personajes_queue)

