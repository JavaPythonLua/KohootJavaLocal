import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = "192.168.1.216"
PORT = 2354
FORMAT = "utf-8"
print(f"The host is {HOST}")
print(f"The port is {PORT}")
s.bind((HOST,PORT))
s.listen()
print("Server is listening...")
while True:
    conn, addr = s.accept()
    print(type(conn))
    print(type(addr))
