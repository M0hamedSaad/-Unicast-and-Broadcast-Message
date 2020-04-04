import socket
import sys

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

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    text = ""
    print("Note:if u need exit to send press [exit]")

    while text != 'exit':
        text = input("send : ")
        sock.sendto(text.encode('ascii'), (host, port))

    sock.close()

print("Unicast press [1] \nBroadcast press [2] \nExit press [0]" )
choose=input("Choose :")

if choose == '1':
    host=input("Set IP for user ,U need send it :  ")
    client(host,port)

elif choose =='2':
    host='192.168.173.255'
    client(host,port)

elif choose =='0':
    sys.exit(1)

else:
    print("Chosse Right from List")


