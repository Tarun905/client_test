import socket
from socket import*
s = socket(AF_INET,SOCK_STREAM)

s.bind(("192.168.0.217",7023))
s.listen(0)
s.settimeout(20)

try:
    c,addr = s.accept()
    c.send(b"if we keep changing dis")
    c.close()
    s.close()
except timeout:
    s.close()








