#TCP server side
import socket



#Create a server side socket IPV4 (AF_INET) adn TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address=socket.gethostbyname(socket.gethostname())
#See how to get IP address dynamically

#print(socket.gethostname())#HostName
#print(socket.gethostbyname(socket.gethostname()))#Get ip address using the Hostname


#Bind our server using IP and Port address

server_socket.bind( (ip_address,5321) )

#Socket to listen incoming connections

server_socket.listen()

#Listen forever to accept ANY incoming connection

while True:
    #Accept every single connection and store the information
    client_socket,client_address = server_socket.accept()
    print(type(client_socket))
    print(client_socket)
    print(type(client_address))
    print(client_address)
    print(f"Alguien se conecto {client_address}!")

    #Send a message to the client
    client_socket.send("Te conectaste".encode())
    server_socket.close()
    break


