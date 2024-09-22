import socket

file = input("Which file? : ")

control = open(file , "r")

content = control.read()

size = len(content)


s = socket.socket(socket.AF_INET , socket.SOCK_STREAM , socket.IPPROTO_TCP)

s.bind( ("127.0.0.1", 2000) )
s.listen()

con, add = s.accept()

size_str = str(size)

print(size)

con.send(size_str.encode())

con.send(content.encode())

s.close()
control.close()
con.close()




