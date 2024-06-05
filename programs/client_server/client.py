import socket

# base important variables
encoding = 'utf-8'
adress = '127.0.0.1'
port = 25565

# runtime variables
is_client_running = True

# Create a socket and connects to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((adress, port))

message = "Hello !".encode(encoding)
s.sendall(message)

while is_client_running:
    message = input(">>> ")
    s.sendall(message.encode(encoding))