import socket

HOST = ''  # localhost
PORT = 3214

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # ipv4

s.bind((HOST, PORT))

data = True  # initial value

while data:
    data, addr = s.recvfrom(1024)  # buffer_size is 1024
    if data == b'bye':  # binary string
        break
    print('Recieve String:', data.decode('utf-8'))
    s.sendto(data, addr)

s.close()