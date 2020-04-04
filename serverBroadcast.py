import socket
port =6000
host =''
BUFFERSIZE =2048

def server(host,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((host,port))
    print('listening to {}.. '.format(sock.getsockname()))

    while True:
        data , address =sock.recvfrom(BUFFERSIZE)
        text =data.decode("ascii")
        print("the client{} says {}".format(address,text))

    sock.close()

server('',6000)