from base64 import encode
from socket import *
serverName = '127.0.0.1'
serverPort = 12000


def main():

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    sentence = input('input lowercase sentence: ')

    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From Server: ', modifiedSentence.decode())
    clientSocket.close()

if __name__ == '__main__':
    main()