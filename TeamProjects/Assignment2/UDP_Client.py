from email import message
from socket import *
from time import sleep
import sys
#serverName = '127.0.0.1'
#serverPort = 12000


def pingaroo(ip, port):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    mess =  'a'
    count = 0;
    miss=0; 

    while count < 10:
        try:
            clientSocket.sendto(mess.encode(), (ip, port))
            modMess, serverAddress = clientSocket.recvfrom(2048)
            print ('pong')    
        except timeout:
            print('timeout')
            miss+=1
        count +=1


    clientSocket.close()

if __name__ == '__main__':
    print(f" ARG1: {sys.argv[1]}")
    print(f" ARG2: {sys.argv[2]}")

    pingaroo(sys.argv[1], int(sys.argv[2]))


