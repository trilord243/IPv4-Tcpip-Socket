#TCP server side
import socket
#Create a server side socket IPV4 (AF_INET) adn TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#See how to get IP address dynamically

print(socket.gethostname())#HostName
print(socket.gethostbyname(socket.gethostname()))#Get ip address using the Hostname