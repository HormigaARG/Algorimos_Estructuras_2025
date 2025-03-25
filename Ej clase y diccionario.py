#1.Escribir una declaración de tipo registro que almacene la sig. información sobre un disco de audio: 
#título, autor, año de publicación y duración en segundos. 
#2. Realizar la declaración de tipo registro para un automóvil: los campos son marca, modelo, año, 
#color, Nº de puertas y precio. 
#3. Escribir un programa que cargue y visualice la información de los registros dados en los puntos 1 y 2

# disco_audio={
    
#     "titulo": None,
#     "autor": None,
#     "año": None,
#     "duracion": None, 
# }

# print("Ingrese los siguiente datos del disco de audio: ")
# disco_audio["titulo"]=input("Titulo: ")
# disco_audio["autor"]=input("Autor: ")
# disco_audio["año"]=input("Año: ")
# disco_audio["duracion"]=input("Duracion: ")

# print("Asi quedaron los datos del disco de audio: ")
# print("titulo: ", disco_audio["titulo"])
# print("autor: ", disco_audio["autor"])
# print("año: ", disco_audio["año"])
# print("duracion: ", disco_audio["duracion"])

class disco_audio:
    titulo, autor, anio, duracion= None, None, None, None
    
discos=disco_audio()

def datos(disco:disco_audio):
    disco.titulo=input("Titulo: ")
    disco.autor=input("Autor: ")
    disco.anio=input("Año: ")
    disco.duracion=input("Duracion: ")
    
def mostrar(disco:disco_audio):
    print(f"El titulo es: {disco.titulo}")
    print(f"El autor es: {disco.autor}")
    print(f"El año es: {disco.anio}")
    print(f"La duracion es: {disco.duracion}")

print("Ingrese los siguientes datos del disco")
datos(discos)
mostrar(discos)