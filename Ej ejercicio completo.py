n=2

class t_poliza:
    def __init__(self, numero: int=0, nombre: str="", direccion: str="", nacimiento: int=0, cant_asegurada: float=0.0, cuota: float=0.0): #Init ejecuta automáticamente cuando se crea un nuevo objeto de una clase
        self.numero = numero #self permite que los métodos de la clase accedan y modifiquen los atributos del objeto
        self.nombre = nombre
        self.direccion = direccion
        self.nacimiento = nacimiento
        self.cant_asegurada = cant_asegurada
        self.cuota = cuota
    
    
v_polizas = [t_poliza() for _ in range(n)] #for _ in range(n) se usa en Python para repetir una acción n veces


# ACA EN LA INICIALIZACION ESTA AL PEDO PORQUE SE INICIALIZA EN LA CLASE MISMA (ARRIBA)!
def inicializar_registro(reg:t_poliza):
    reg.numero=0
    reg.nombre=""
    reg.direccion=""
    reg.nacimiento=0
    reg.cant_asegurada=0
    reg.cuota=0
    
def inicializar_vector(v_pol=v_polizas):
    for j in range(0,n):
        inicializar_registro(v_pol[j])
        
def cargar_registro(reg:t_poliza):
    reg.numero=int(input("Numero: "))
    reg.nombre=input("Nombre: ")
    reg.direccion=input("Direccion: ")
    reg.nacimiento=int(input("Nacimiento: "))
    reg.cant_asegurada=float(input("Cantidad asegurada: "))  
    reg.cuota=float(input("Cuota: "))
    
def cargar_vector(v_pol=v_polizas):
    for j in range(0,n):
        print(f"Ingrese los siguientes datos de la poliza {j}:")
        cargar_registro(v_pol[j])


def mostrar_registro(reg:t_poliza):
    print(f"Numero: {reg.numero}")
    print(f"Nombre: {reg.nombre}")
    print(f"Direccion: {reg.direccion}")
    print(f"Nacimiento: {reg.nacimiento}")
    print(f"Cantidad asegurada: {reg.cant_asegurada}")
    print(f"Cuota: {reg.cuota}")
    
def mostrar_vector(v_pol=v_polizas):
    for j in range(0,n):
        print()
        print(f"ESTOS SON LOS DATOS DE LA POLIZA {j} ")
        mostrar_registro(v_pol[j])
    
#ORDENAR POR NOMBRE
def ordenar_burbuja(v_pol=v_polizas):
    aux:t_poliza
    for i in range(0,n):
        for j in range(0,n-1-i): #Aca es n-1 porque como arranca en cero hay que tener en cuenta que sino se desborda
            if (v_pol[j].nombre)>(v_pol[j+1].nombre):
                aux=v_pol[j]
                v_pol[j]=v_pol[j+1]
                v_pol[j+1]=aux

def busqueda(v_pol=v_polizas):
    for j in range(0,n):
        if (v_pol[j].nombre=="Axel Sandillu"):
            print()
            print("Se encontro a Axel Sandillu en la compañia")
    
    
    
    
    
#BEGIN
inicializar_vector(v_polizas)
cargar_vector(v_polizas)
ordenar_burbuja(v_polizas)
mostrar_vector(v_polizas)
busqueda(v_polizas)


#END

