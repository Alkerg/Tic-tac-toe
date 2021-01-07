from random import randint

#VARIABLES
jugando = True
tablero = [[1,2,3],[4,"X",6],[7,8,9]]
columna = ""
invalido = ""

#FUNCTIONS
def dibujarTablero():
    for i in range(3):
        print("+-------+-------+-------+")
        print("|","|","|","|", sep="       ")
        print("|", end="")
        for j in range(3):
            print("",tablero[i][j], end="   |", sep="   ")
        print("\n","","","","", end="\n", sep="|       ")
    print("+-------+-------+-------+")
                
def turnoJugador():
    global columna
    global invalido
    columna = ""
    if movJugador <= 3:
         fila = 0
    elif movJugador > 3 and movJugador < 7:
         fila = 1
    else:
         fila = 2
    for j in range(3):
        if movJugador == tablero[fila][j]:
            columna = j
    if columna != "":
        tablero[fila][columna] = "O"
        dibujarTablero()
        invalido = False
    else:
        invalido = True

def turnoBot():
    global jugando
    global invalido
    ocupado = True
    while ocupado and not invalido:
        movBot = randint(1,9)
        for i in range(3):
            for j in range(3):
                if movBot == tablero[i][j]:
                    tablero[i][j] = "X"
                    ocupado = False
    if jugando:
        dibujarTablero()
   
def comprobarGanador():
    global jugando
    if tablero[0][0] == tablero[0][1] == tablero[0][2]:
        terminarPartida(tablero[0][0])
    elif tablero[1][0] == tablero[1][1] == tablero[1][2]:
        terminarPartida(tablero[1][0])
    elif tablero[2][0] == tablero[2][1] == tablero[2][2]:
        terminarPartida(tablero[2][0])
    elif tablero[0][0] == tablero[1][0] == tablero[2][0]:
        terminarPartida(tablero[0][0])
    elif tablero[0][1] == tablero[1][1] == tablero[2][1]:
        terminarPartida(tablero[0][1])
    elif tablero[0][2] == tablero[1][2] == tablero[2][2]:
        terminarPartida(tablero[0][2])
    elif tablero[0][0] == tablero[1][1] == tablero[2][2]:
        terminarPartida(tablero[0][0])
    elif tablero[0][2] == tablero[1][1] == tablero[2][0]:
        terminarPartida(tablero[0][2])
    else:
        terminarPartida(0)

def terminarPartida(ficha):
    global jugando
    if jugando:      
        if ficha == "X":
            print("¡Has Perdido! :(")
            jugando = False
        elif ficha == "O":
            print("¡Has Ganado! :)")
            jugando = False
        else:
            fichas = 0
            for i in range(3):
                for j in range(3):
                    if type(tablero[i][j]) != int:
                        fichas +=1
                if fichas == 9:
                    print("¡Empate!")
                    jugando = False
            
#MAIN RUN
print("¡A jugar!")
dibujarTablero()

while jugando:
    movJugador = int(input("Ingresa tu movimiento: "))
    if(movJugador > 0 and movJugador < 10):
        turnoJugador()   
        comprobarGanador()
        turnoBot()
        comprobarGanador()
    else:
        print("Por favor, introduce un numero del 1 al 9")
        continue

input("Presiona ENTER  para salir")