

def lobby(socket, delim):

    socket.send("LOBBIES".encode())
    response = socket.recv(1024).decode()
    data = response.split(delim)
    if data[0] == "LOBBIES":
        print("Available lobbies: ")
        for index, lobby_name in enumerate(data[1:]):
            print(str(index + 1) + ":", lobby_name)

        lobby_index = int(input("select lobby id to join, 0 to refresh"))
        if lobby_index == 0:
            return lobby(socket, delim)
        else:
            return data[lobby_index]


