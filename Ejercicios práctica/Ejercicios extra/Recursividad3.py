def ping(x):
    if x > 10:
        return  # Detiene la recursión cuando x es mayor que 10
    else:
        print("Ping", x)
        pong(x + 1)  # Llama a `pong` con x incrementado

def pong(x):
    if x > 10:
        return  # Detiene la recursión cuando x es mayor que 10
    else:
        print("Pong", x)
        ping(x + 1)  # Llama a `ping` con x incrementado

ping(1)