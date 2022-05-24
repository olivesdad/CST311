import threading
import time
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

class SharedData:
    
    def __init__(self):
        
        messages = {
            "c1" : "",
            "c2" : ''
        }
        C1Full = False
        C2Full = False

def connect(name, socket, data):
    if name == 'c1':
        print('im c1')
    elif name == 'c2':
        print('im c2')
    else:
        print('unknown client error')


def Main():

    print('main done')
    
if __name__ == '__main__':
    Main()