#UDP Server side

import socket



#Create a server side socket IPV4(AF_INET) and UDP  (SOCK_DGRAM)

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#Bind new socket to a tuple ip and port


server_socket.bind((socket.gethostbyname(socket.gethostname()),59696))

#We are not listening or accepting connect since UDP is conectionless protocol

message,address=server_socket.recvfrom(1024)
print(message.decode())
print(address)
