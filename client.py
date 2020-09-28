import socket 

HOST = '127.0.0.1'
PORT = 54321 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, 65432))
    s.sendall(b'Testing this works')
    data = s.recv(1024)

print('received', repr(data))