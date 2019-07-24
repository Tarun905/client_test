import socket
from socket import*
s = socket(AF_INET,SOCK_STREAM)

s.connect(("192.168.0.111",7019))


while True:
    inpu = input(">").encode()
    s.send(inpu)

var = s.recv(1024)
print(var)
s.close()





























































































