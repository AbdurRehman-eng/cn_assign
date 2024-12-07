import socket

def recvFile ( file_path, host = "127.0.0.1", port = 5000):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', port))

    print(s.recv(1024).decode())

    s.close()