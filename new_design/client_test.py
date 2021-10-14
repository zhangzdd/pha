import socket

client = socket.socket()

ip_port = ("127.0.0.1", 6688)
client.connect(ip_port)

while True:
    data = client.recv(1024)
    print(data.decode())
    data = client.recv(1024)
    print(data.decode())