from email import message
from socket import *
serverName = '127.0.0.1'
serverPort = 3033
clientSocket = socket(AF_INET, SOCK_DGRAM)
mess = input("input lowecase sentence: ")

clientSocket.sendto(mess.encode(), (serverName, serverPort))

modMess, serverAddress = clientSocket.recvfrom(2048)

print (modMess.decode())
clientSocket.close()
