import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

while True:
    print(s.recvfrom(65535))
