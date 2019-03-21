import socket
def Main():
    host="192.168.225.243"
    port=5004
    mysocket= socket.socket()
    mysocket.connect((host,port))
    message= input("?")
    while message!='q':
        mysocket.send(message.encode())
        data= mysocket.recv(1024).decode()
        print('recived from server: '+data)
        message= input('?')
    mysocket.close
    
Main()


