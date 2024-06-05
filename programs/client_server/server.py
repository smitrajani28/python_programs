import socket
import threading

# Some base important value
ip = '0.0.0.0'
port = 25565
encoding = 'utf-8'

# Some runtime value
clientList = []
is_server_running = True


# a class representing a client
class ClientThread(threading.Thread):
    conn = None
    addr = None

    # Use to init the thread and the main client value
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)

        self.conn = conn
        self.addr = addr

        print(f"Successfully created client thread for client {self.addr[0]}:{self.addr[1]}")

    # Use to receive and send data
    def run(self):
        while True:
            try:
                data = self.conn.recv(1024).decode(encoding)
                print(f"Got message from client ({self.addr[0]}:{self.addr[1]}) : \"{data}\"")
            except Exception as e:
                print(f"Got exception in client {self.addr[0]}:{self.addr[1]} : {str(e)}")
                break

        clientList.remove(self)


# Create a socket and bind the correct port and ip
print("Creating Server...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(5)

print(f"Server created and launched on port {port}.")

while is_server_running:
    try:
        # Accept the connection and create a new client thread
        conn, adrr = s.accept()

        print(f"Got new connection from adress {adrr[0]}:{adrr[1]}. Creating Thread for client")

        client_thread = ClientThread(conn, adrr)
        client_thread.start()

        clientList.append(client_thread)
    except Exception as e:
        print(f"Got Exception in server listening runtime : {str(e)}. Server Stopped")
        is_server_running = False
        break


for client in clientList:
    client.conn.close()

s.close()