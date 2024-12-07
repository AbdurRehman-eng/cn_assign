import socket
import os
import json

def sendFile ( file_path, host = '0.0.0.0', port = 5000 ):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("TCP socket created successfully")

    s.bind((host, port))
    s.listen(1)
    print(f"Server listening on Host: {host} and Port: {port}")
    con, addr = s.accept()
    print(f"Sending file to {addr}")

    sep = "."
    fragCount = 0
    fileExten = file_path[file_path.rfind(sep):]
    fileSize = os.path.getsize(file_path)
    fragSize = 1024

    metadata = {
        'fileSize' : fileSize,
        'fragSize' : fragSize
    }

    jsonMeta = json.dumps(metadata)

    with open(file_path, "rb") as file:
        con.sendall(fileExten.encode())
        con.sendall(str(fragSize).encode())
        con.sendall(jsonMeta.encode())
        print("metadata sent")
        while fragment := file.read(fragSize):
            print(f"Sending fragment {fragCount}")
            con.sendall(fragment)
            # con.sendall(str(fragCount).encode())
            fragCount += 1

    print("File sent successfully.")
    con.close()

sendFile("D:\\Projects\\cn_assign\\video\\new.tif")