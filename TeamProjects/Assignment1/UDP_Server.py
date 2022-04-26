from email import message
from http import client
from operator import truediv
from socket import *
serverPort=12000
serverSocket=socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("The server is ready")
while True:
    message, clientAddress=serverSocket.recvfrom(2048)
    modifiedMessage=message.decode().upper()
    serverSocket.sento(modifiedMessage.encode(), clientAddress)
