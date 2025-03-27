n=5
t_vector=[0] * n

numeros=t_vector


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


#BEGIN
inicializar_vector(numeros)
cargar_vector(numeros)
print()
mostrar_vector(numeros)

#END