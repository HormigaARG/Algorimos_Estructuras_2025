n=3
t_vector=[0] * n

numeros=t_vector
limite=0

#INICIALIZAR VECTOR/LISTA
def inicializar_vector(num):
    for i in range(0,n):
        num[i]=0
        
#CARGAR VECTOR/LISTA
def cargar_vector(num):
    global limite # Usamos la variable global 'limite' para modificarla
    
    opcion=(input("Desea ingresar un numero al vector? S/N: ")).upper() #upper es para MAYUS
    while opcion=="S" and limite<n:
        aux=int(input(f"Ingrese un numero al vector en la posicion {limite}: "))
        num[limite]=aux
        limite+=1
    
        if limite < n:  # Solo preguntar si hay espacio en el vector
            opcion = input("Desea volver a ingresar otro numero al vector? S/N: ").upper() #upper es para MAYUS
    
        
#MOSTRAR VECTOR/LISTA
def mostrar_vector(num):
    for i in range(0,limite):
        print(f"El elemento que esta en la posicion {i} es: {num[i]}")


#BEGIN

inicializar_vector(numeros)
cargar_vector(numeros)
print()
mostrar_vector(numeros)

#END