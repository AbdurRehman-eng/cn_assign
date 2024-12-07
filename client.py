import socket

def recvFile ( file_path, host = "127.0.0.1", port = 5000):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    print("connection successful!.")

    with open(file_path, "wb") as file:
        while True:
            frag = s.recv(1024)
            if not frag:
                break
            file.write(frag)
    
    print(f"File received and saved to {file_path}")
    s.close()

recvFile("ne.tif")