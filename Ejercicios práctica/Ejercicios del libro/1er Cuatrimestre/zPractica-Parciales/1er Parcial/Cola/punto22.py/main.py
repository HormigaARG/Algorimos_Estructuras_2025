# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) 
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

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
def determinarNombreSH(perso_queue):
    aux_queue=Queue()
    encontrado=False
    
    while perso_queue.size()>0:
        pj=perso_queue.attention()
        aux_queue.arrive(pj)
        
        if pj.nombreSH=="Capitana Marvel":
            encontrado=True
            print(f"Nombre del personaje de la superhéroe Capitana Marvel: {pj.nombrePJ}")
            
            
    if not encontrado:
        print("No se pudo encontrar la superHeroe Capitana Marvel.")
        
    while aux_queue.size()>0:
        perso_queue.arrive(aux_queue.attention())
        
# b. mostrar los nombre de los superhéroes femeninos;
def determinarNombreFemeninos(perso_queue):
    aux_queue=Queue()
    
    while perso_queue.size()>0:
        pj=perso_queue.attention()
        aux_queue.arrive(pj)
        
        if pj.genero=="F":
            print(f"{pj.nombreSH}")
        
        
    while aux_queue.size()>0:
        perso_queue.arrive(aux_queue.attention())
        
# c. mostrar los nombres de los personajes masculinos;        
def determinarNombreMasculinos(perso_queue):
    aux_queue=Queue() #cola auxiliar para reponer cola original
    while perso_queue.size()>0:
        pj=perso_queue.attention()
        aux_queue.arrive(pj)
        
        if pj.genero=="M":
            print(f"{pj.nombrePJ}")
            
    while aux_queue.size()>0: #restauro la cola original
        perso_queue.arrive(aux_queue.attention())
               
               
# d. determinar el nombre del superhéroe del personaje Scott Lang;
def determinarNombreSH(perso_queue):
    aux_queue=Queue() #cola auxiliar para reponer cola original
    encontrado=False
    while perso_queue.size()>0:
        pj=perso_queue.attention()
        aux_queue.arrive(pj)
        
        if pj.nombrePJ=="Scott Lang":
            encontrado=True
            print(f"{pj.nombreSH}")
            
    if not encontrado:
        print("No se ha encontrado al personaje Scott Lang.")
        
        
        
    while aux_queue.size()>0: #restauro la cola original
        perso_queue.arrive(aux_queue.attention())
   
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
def mostrarDatosLetraS(perso_queue):
    aux_queue=Queue() #cola auxiliar para reponer cola original
    while perso_queue.size()>0:
        pj=perso_queue.attention()
        aux_queue.arrive(pj)
        
        if pj.nombrePJ.startswith("S") or pj.nombreSH.startswith("S"):
            print(pj)
        
    while aux_queue.size()>0: #restauro la cola original
        perso_queue.arrive(aux_queue.attention())
        
        
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.
def determinarPersonajeEspecifico(perso_queue):
    aux_queue=Queue() #cola auxiliar para reponer cola original
    encontrado=False
    while perso_queue.size()>0:
        pj=perso_queue.attention()
        aux_queue.arrive(pj)
        
        if pj.nombrePJ=="Carol Danvers":
            encontrado=True
            print(f"Se encontro a Carol Danvers en la cola!, su nombre Super Heroe es: {pj.nombreSH}")
            
    if not encontrado:
        print("No se encontro al personaje de Caron Danvers en la cola.")
        
        
    while aux_queue.size()>0: #restauro la cola original
        perso_queue.arrive(aux_queue.attention())
        
#CP
cargarCola(personajes_queue, personajes)
determinarNombreSH(personajes_queue)
print()
print("Nombre de los superheroes femeninos: ")
determinarNombreFemeninos(personajes_queue)
print("Nombre de los personajes masculinos: ")
determinarNombreMasculinos(personajes_queue)
print()
print("Nombre del superhéroe del personaje Scott Lang:")
determinarNombreSH(personajes_queue)
print()
print("Todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S: ")
mostrarDatosLetraS(personajes_queue)
print()
determinarPersonajeEspecifico(personajes_queue)



        