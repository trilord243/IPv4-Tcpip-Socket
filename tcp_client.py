#TCP client side

import socket
#Creat client side IPV4 socket (AF_INET) and TCP (SOCKET_STREAM)
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connect the socket to a server located at a given IP and Port

client_socket.connect((socket.gethostbyname(socket.gethostname() ), 5321))

#Recibi el mensaje del servidor se debe espeicifar el mayor numero de bytes

message= client_socket.recv(1024)

print(message.decode())

#Cerrar socket
client_socket.close()
