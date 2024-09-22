import socket

file = input("Which filename to create? : ")

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM , socket.IPPROTO_TCP)

try:
    s.connect( ("3.125.188.168" , 10160) )
except ConnectionRefusedError:
    print("Connection refused by sender.")

size_str = s.recv(10)

size_str = size_str.decode()

size = int(size_str)

print(size)

data = s.recv(size)

print(data.decode())

s.close()

data = data.decode()

controller = open(file, "w")

controller.write(data)

controller.close()


