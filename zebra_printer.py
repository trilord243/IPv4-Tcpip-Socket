import socket


client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


client_socket.connect( ("192.168.1.225",9100))

client_socket.send('{}{"device.friendly_name":null}'.encode() )
client_socket.send("""^XA
^FO50,50
^A0N,50,50
^FDHola Mundo^FS
^XZ""".encode())

try:
    message =client_socket.recv(1024)
    print(message.decode())
except socket.timeout:
    print("No se recibio el mensaje ")


client_socket.close()