import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = str(input("Host: "))
PORT = int(input("Port: "))
s.connect((HOST,PORT))
msg = s.recv(1024)
print(msg)