# 3c.CREATION FOR FILE TRANSFER USING TCP SOCKETS
## AIM
To write a python program for creating File Transfer using TCP Sockets Links
## ALGORITHM:
1. Import the necessary python modules.
2. Create a socket connection using socket module.
3. Send the message to write into the file to the client file.
4. Open the file and then send it to the client in byte format.
5. In the client side receive the file from server and then write the content into it.
## PROGRAM
## server:
```
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
```
## client:
```
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
```
## OUPUT
![alt text](<Screenshot 2025-10-27 215704.png>)
## RESULT
Thus, the python program for creating File Transfer using TCP Sockets Links was 
successfully created and executed.
