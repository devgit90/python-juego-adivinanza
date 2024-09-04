import random


def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego de adivinanza de número. ")
    print("Debes adivinar un número de entre 1 y 100")
    print("Intenta adivinarlo")

    while not adivinado:
        adivinanza = input("Introduzca número entre 1 y 100 ->  ")

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(
                    f"Felicidades has ganado el número {adivinanza} es el secreto y lo has logrado en el intento {intentos}"
                )
        else:
            print("Por favor introduzca un número valido entre 1 y 100")


juego_adivinanza()
