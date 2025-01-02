
#UDP client side
import socket


#Create a UDP IPV4 socket

client_socket= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Send some info vie UPD protocol

client_socket.sendto("Hello server".encode(), (socket.gethostbyname(socket.gethostname()),59696  ) )

