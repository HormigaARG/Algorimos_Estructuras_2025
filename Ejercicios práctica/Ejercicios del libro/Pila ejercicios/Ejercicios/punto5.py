#5. Determinar si una cadena de caracteres es un palíndromo.
from stack import Stack
cadenas_stack = Stack()

for i in range(4):
   cadenaIngresa=str(input(f"Ingrese la cadena {i} para ver si es palindromo: "))
   cadenas_stack.push(cadenaIngresa)
   
def verificarPalindromo(cad_stack):
   palindromo_stack=Stack()
   for i in range(cad_stack.size()):
      cadena=cad_stack.pop() #guardo el valor de la pila segun su posicion
      cadena_invertida=cadena[::-1] #invierto la cadena que esta apilada en la pila
      if cadena==cadena_invertida: #comparo si son iguales
         palindromo_stack.push(cadena)  
   return palindromo_stack
      
      
print("Pila Cargada: ")
cadenas_stack.show()
print()
print("La pila con cadenas que son palindromo: ")
cadenas_stack=verificarPalindromo(cadenas_stack)
cadenas_stack.show()
