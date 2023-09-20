import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9000))

comando = "GET http://example.com/index.html HTTP/1.0\r\n\r\n".encode()
client.send(comando)

while True:
    data = client.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

client.close()