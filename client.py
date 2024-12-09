import socket
import threading
import math

fragPerServer = 0

def recvFile ( fileName, servers, serverNo, host = "127.0.0.1", port = 5000 ):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("connection successful")

    global fragPerServer
    fileExten = s.recv(1024).decode().strip('\x00') 
    fragSize = int.from_bytes(s.recv(1024), byteorder='big')
    fileSize = int.from_bytes(s.recv(1024), byteorder='big')
    totalFrag = math.ceil(fileSize/fragSize)
    print("metadata received")

    fragPerServer = math.ceil(totalFrag/servers)
    s.sendall(fragPerServer.to_bytes(1024, byteorder='big'))
    print("fragments per server sent successfully")

    s.sendall(serverNo.to_bytes(1024, byteorder='big'))
    print("server number sent successfully")
    
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

def fileCombine(files, fragSize, fragPerFile):
    for i in files:
        with open(i, "rb") as file:
            with open("new.tif", "ab") as newFile:
                while True:
                    buff = file.read(fragSize*fragPerFile)
                    if not buff:
                        break
                    newFile.write(buff)
    print("File combined successfully")

threads = [
    threading.Thread(target=recvFile, args=("k", 5, 0, "127.0.0.1", 5000)),
    threading.Thread(target=recvFile, args=("l", 5, 1, "127.0.0.1", 5100)),
    threading.Thread(target=recvFile, args=("j", 5, 2, "127.0.0.1", 5200)),
]

files = [
    "j.tif",
    "k.tif",
    "l.tif"
]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("All files received")

fileCombine(files, 1024, fragPerServer)
