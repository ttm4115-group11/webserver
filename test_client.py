import socket

address = ''
port = 5001
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((address, port))
s.listen(1)

conn, addr = s.accept()

while 1:
    data = conn.recv(buffer_size)
    print(data)
