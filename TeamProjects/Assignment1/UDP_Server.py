from email import message
from http import client
from operator import truediv
from socket import *
serverPort=12000
serverSocket=socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("The server is ready")
while True:
    mess, clientAddress=serverSocket.recvfrom(1024)
    modifiedMessage=mess.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
