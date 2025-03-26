n=6
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

#ORDENAR (ASCENDIENTE) VECTOR/LISTA
def ordenar_vector1(num):
    num.sort() 
    
#ORDENAR (DESCENDIENTE) VECTOR/LISTA
def ordenar_vector2(num):
    num.sort(reverse=True)

#BUSCAR LA POSICION DEL NUMERO
def buscar_posicion(num):
    global posicion # Usamos la variable global 'posicion' para modificarla
    posicion=num.index(buscado) #Index devuelve la posicion donde esta ese numero
    


#BEGIN
buscado=30
posicion=0
inicializar_vector(numeros)
cargar_vector(numeros)
print()
ordenar_vector1(numeros)
print("Vector ordenado de forma ascendiente: ")
mostrar_vector(numeros)
ordenar_vector2(numeros)
print("Vector ordenado de forma descendiente: ")
mostrar_vector(numeros)
print()
buscar_posicion(numeros)
print(f"El numero buscado: {buscado} se encuentra en el vector en la posicion {posicion}")

#END