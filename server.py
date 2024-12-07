import socket

def sendFile ( file_path, host = '0.0.0.0', port = 5000 ):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("TCP socket created successfully")

    s.bind((host, port))
    s.listen(1)
    print(f"Server listening on Host: {host} and Port: {port}")
    con, addr = s.accept()
    with open(file_path, "rb") as file:
        while fragment := file.read(1024):
            con.sendall(fragment)
    print("File sent successfully.")
    con.close()

sendFile("/video/new.tif")