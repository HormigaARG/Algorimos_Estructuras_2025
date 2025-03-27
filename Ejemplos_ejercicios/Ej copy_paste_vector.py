n=5
t_vector=[0] * n

numeros=t_vector
numeros2=t_vector


#INICIALIZAR VECTOR/LISTA
def inicializar_vector(num):
    for i in range(0,n):
        num[i]=0


#CARGAR VECTOR/LISTA
def cargar_vector(num):
    for i in range(0,n):
     num[i]=(input(f"Ingrese un numero en la posicion {i}: "))
        
#MOSTRAR VECTOR/LISTA
def mostrar_vector(num):
    for i in range(0,n):
        print(f"El elemento que esta en la posicion {i} es: {num[i]}")
        
#COPIAR Y PEGAR VECTOR
def copiar_pegar_vector(num,num2):
    for i in range(0,n):
        num2[i]=num[i]



#BEGIN
inicializar_vector(numeros)
inicializar_vector(numeros2)
cargar_vector(numeros)
copiar_pegar_vector(numeros,numeros2)
print()
mostrar_vector(numeros)
print()
print("VECTOR COPIADO Y PEGADO: ")
mostrar_vector(numeros2)
#END