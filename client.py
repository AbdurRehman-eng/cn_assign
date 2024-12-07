import socket
import json

def recvFile ( fileName, host = "127.0.0.1", port = 5000):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    print("connection successful!.")

    fileExten = s.recv(1024).decode()
    fragSize = s.recv(1024).decode()
    # fileSize = int(s.recv(1024).decode())
    metadata_size = int(s.recv(4).decode())
    metadata = b''
    while len(metadata) < metadata_size:
        metadata += s.recv(1024)
    metadata = json.loads(metadata.decode())  # Now decode the complete metadata
    fileSize = metadata['fileSize']


    print("metadata received")
    file_name = fileName + fileExten

    with open(file_name, "wb") as file:
        while True:
            frag = s.recv((int(fragSize)))
            # fragCount = int(s.recv(1024).decode())
            # print(f"Received fragment No. {fragCount}")
            if not frag:
                break
            file.write(frag)
    
    print(f"File received and saved as {file_name}")
    s.close()

recvFile(input("Enter the name of the file(without extension): "))