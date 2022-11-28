import socket
import select
import time

# Creation of the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 6007))
server_socket.listen()
(client_socket, client_address) = server_socket.accept()
time.sleep(10)
while True:

     #Receive the data from R
    data = client_socket.recv(1024)
    str = data.decode('ascii')
    print(str)

    # Send data to R
    what_to_send = 'Hello ' + data.decode()
    client_socket.send(what_to_send.encode())

#Close the socket
#client_socket.close()
#server_socket.close()