import socket
import time
def Main():
    host="192.168.43.106"
    port=5004
    mysocket= socket.socket()
    mysocket.bind((host,port))
    mysocket.listen(1)
    conn,addr= mysocket.accept()
    print("connection from:"+ str(addr))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user:"+str(data))
        data=input("?")
        conn.send(data.encode())
    conn.close
    
Main()
