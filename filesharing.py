import os

print("Welcome to the file sharing python project!!!")

na = input("Are you gonna be the sender or reciever ? ")
na = na.lower()

while True:
    if na == "s" or na == "sender" :
        os.system("python3 base\\sender.py")
        break

    elif na == "r" or na == "reciever" : 
        os.system("python3 base\\reciever.py")
        break

    else:
        print("Unknown role. Please try again")
        na = input("Are you the sender or reciever?")