import socket
import json

def recvFile ( fileName, host = "127.0.0.1", port = 5000):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    print("connection successful!.")

    fileExten = s.recv(1024).decode()
    fragSize = int.from_bytes(s.recv(1024), byteorder='big')
    # fileSize = int(s.recv(1024).decode())

    print("metadata received")
    file_name = fileName + fileExten

    with open(file_name, "wb") as file:
        while True:
            frag = s.recv((fragSize))
            fragCount = int.from_bytes(s.recv(1024), byteorder='big')
            print(f"Received fragment No. {fragCount}", end="\r")
            if not frag:
                break
            file.write(frag)
    
    print(f"File received and saved as {file_name}")
    s.close()

recvFile(input("Enter the name of the file(without extension): "))