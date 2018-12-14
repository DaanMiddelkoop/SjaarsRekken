from board import Board
import pygame
import time
import socket
from lobby import lobby

delim = " "


def convert_color_to_dres_kekke_conventies(tupleding):
    x, y, top, left, right = tupleding
    if y % 2 == x % 2:
        #top is down
        return left, right, top
    return right, left, top


def deconvert_dres_stupide_kleur_assignments_voor_stomme_scheef_gedefineerde_triangles(x, y, k1, k2, k3):
    if y % 2 == x % 2:
        return k3, k1, k2
    return k3, k2, k1


def main():

    pygame.init()

    name = input("Enter name")
    server_ip = input("Enter ip")
    port = int(input("Enter port"))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, port))
    sock.send(("CONNECT" + delim + name).encode())
    sock.send("WTF????".encode())

    print("printed wtf string")

    #TRY HANDSHAKING
    response = str(sock.recv(1024).decode())
    if not response:
        print("server has not responded to handshake attempt\n")
        return
    elif response == "CONFIRM":
        print("Handshake complete, connected successfully")
    else:
        print("Server refused us")
        return

    chosen_lobby = lobby(sock, delim)
    sock.send(("JOIN" + delim + chosen_lobby).encode())

    input("press enter to state readyness")

    sock.send("READY".encode())

    num_players = 0
    while True:
        response = sock.recv(1024).decode().split(delim)
        if response[0] == "GAME" and response[1] == "START":
            player_list = response[2:]
            print("Game starting: connected players: ", player_list)
            num_players = len(response[2:])
            break

    screen = pygame.display.set_mode((1280, 720))

    board = Board()

    while True:
        response = sock.recv(1024).decode().split(delim)
        print(response)
        if response[0] == "GAME":
            if response[1] == "MOVE":
                if response[2] == name:
                    # we dont care about our own move :)
                    continue
                print("player", response[2], "made move ", response[3], response[4], response[5], response[6], response[7], "next player: ", response[8])
                top, left, right = deconvert_dres_stupide_kleur_assignments_voor_stomme_scheef_gedefineerde_triangles(response[3], response[4], response[5], response[6], response[7])
                board.do_move_xy(response[3], response[4], top, left, right)

                if response[8] == name:
                    print("Our turn")

                    move = board.generate_move()
                    if move is None:
                        print("No moves available for us")
                        continue
                    x, y, _, _, _ = move
                    colors = convert_color_to_dres_kekke_conventies(move)

                    sock.send((str(x) + delim + str(y) + delim + colors[0] + delim + colors[1] + delim + colors[2]).encode())
                    print("move made: ", move)
            if response[1] == "END":
                if response[2] == "DRAW":
                    print("The game ended in a draw omg")
                elif response[2] == name:
                    print("As expected, we won :)")
                else:
                    print("Somehow", response[2], "won....")
                break

        board.draw(screen)

        pygame.display.flip()

    while True:
        time.sleep(2)

main()