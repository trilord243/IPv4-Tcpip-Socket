import socket


client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


client_socket.connect( ("192.168.1.225",9100))

client_socket.send(""" ^XA
^FO50,50
^A0N,50,50
^FDHola Mundo^FS
^XZ""".encode() )

client_socket.close()