import socket
HOST = ''
PORT = 3214
s = socket.socket()
s.bind((HOST, PORT))
s.listen(5)
client, addr = s.accept()  # wait client connection ,block......
print("Client Address:", addr)

while True:
    data = client.recv(1024)
    if not data:
        break
    print('Recieve Data:', data.decode('utf-8'))
    client.send(data)

client.close()
s.close()