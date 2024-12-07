import socket

def recvFile ( fileName, host = "127.0.0.1", port = 5000):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    print("connection successful!.")
    fileExten = s.recv(1024).decode()

    file_name = fileName + fileExten

    with open(file_name, "wb") as file:
        while True:
            frag = s.recv(1024)
            if not frag:
                break
            file.write(frag)
    
    print(f"File received and saved as {file_name}")
    s.close()

fileName = input("Enter the name of the file(without extension): ")
recvFile(fileName)