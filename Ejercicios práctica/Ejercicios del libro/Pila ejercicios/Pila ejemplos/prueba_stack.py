from random import randint

from stack import Stack

number_stack = Stack()
even_stack = Stack() # par
odds_stack = Stack() # impares


for i in range(5):
    rand_number = randint(1, 100)
    print(rand_number)
    number_stack.push(rand_number)


# for i in range(number_stack.size()):
while number_stack.size() > 0:
    number = number_stack.pop()
    if number % 2 == 0:
        even_stack.push(number)
    else:
        odds_stack.push(number)

print("pila par: ")
even_stack.show()
print()
print("pila impar:")
odds_stack.show()

print()
print(even_stack.size(), odds_stack.size())
