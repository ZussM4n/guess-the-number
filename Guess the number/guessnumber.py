import random

intentos = 0
maximo = 0
clave = 0

intentosMax = int(input("¿How many tries do you want?"))
maximo = int(input("Say me the maximun number: "))
clave= random.randint(1, maximo)

while True:
    intentos += 1
    if intentos > intentosMax:
        print("You have no more tries left")
        print("END OF THE GAME")
        break
    
    prueba = int(input("Guess the number!"))

    if clave == prueba:
        print("¡You win!",clave)
        print("END OF THE GAME")
        break
    elif clave > prueba:
        print("It's a higher number")
        print("Try again")
    else:
        print("It's a lower number")
        print("Try again")