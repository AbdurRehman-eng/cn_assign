import socket
import os

def sendFile ( file_path, host = '0.0.0.0', port = 5300 ):
    
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

    with open(file_path, "rb") as file:
        con.sendall(fileExten.encode())
        con.sendall(fragSize.to_bytes(1024, byteorder='big'))
        con.sendall(fileSize.to_bytes(1024, byteorder='big'))
        print("metadata sent")
        while fragment := file.read(fragSize):
            print(f"Sending fragment {fragCount}", end="\r")
            con.sendall(fragment)
            con.sendall(fragCount.to_bytes(1024, byteorder='big'))
            fragCount += 1

    print("File sent successfully.")
    con.close()

sendFile("D:\\Projects\\cn_assign\\video\\new.tif")