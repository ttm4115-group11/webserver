import socket

address = '167.99.217.172'
port = 5001
buffer_size = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((address, port))
s.listen(1)

conn, addr = s.accept()

data = conn.recv(buffer_size)
print(addr,data)
    