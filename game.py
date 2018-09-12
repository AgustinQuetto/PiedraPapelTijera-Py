from random import randint
 
#crea un vector de elecciones
elecciones = ["Piedra", "Papel", "Tijeras"]
 
#inicia el jugador en falso
jugador = True
 
while jugador:
    print("\nPiedra, Papel o Tijeras?")
    jugador = input("Escribe tu eleccion: ")
    #asignamos un indice aleatorio para la eleccion de la computadora
    computadora = elecciones[randint(0,2)]

    if jugador == computadora:
        print("Empate")
    elif jugador == "Piedra":
        if computadora == "Papel":
            print("Has perdido", computadora, "envuelve", jugador)
        else:
            print("Has ganado", jugador, "aplasta", computadora)
    elif jugador == "Papel":
        if computadora == "Tijeras":
            print("Perdiste", computadora, "corta", jugador)
        else:
            print("Has ganado", jugador, "envuelve", computadora)
    elif jugador == "Tijeras":
        if computadora == "Piedra":
            print("Has perdido", computadora, "aplasta", jugador)
        else:
            print("Ganaste", jugador, "corta", computadora)
    else:
        print("Le pifeaste a la eleccion.")

    continuar = input('Desea continuar? Si/No: ')

    if(continuar != 'Si'):
      jugador = False

print('Saliste del juego. Gracias por jugar. Vuelve pronto.')
