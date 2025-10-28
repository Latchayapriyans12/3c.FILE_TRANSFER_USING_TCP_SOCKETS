import socket

port = 60000
s = socket.socket()
host = socket.gethostname()

s.bind((host, port))
s.listen(5)
print("Server listening...")

while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    
    data = conn.recv(1024)
    print("Server received:", repr(data))

    filename = 'mytext.txt'  # The file you want to send
    try:
        with open(filename, 'rb') as f:
            l = f.read(1024)
            while l:
                conn.send(l)
                l = f.read(1024)
        print("File sent successfully.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found in current directory.")
    
    conn.close()
    break