import socket

s = socket.socket()
host = socket.gethostname()
port = 60000

s.connect((host, port))
s.send(b'Hello server!')

with open('received_file.txt', 'wb') as f:
    print("File opened for writing.")
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data)
print("File received successfully.")

s.close()