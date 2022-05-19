# Names: Juli Shinozuka, Nadia Rahbany, Kevin McNulty, Andrew Shiraki
# Date: May 16, 2022
# Description: This is a UDP server program that echos in uppercase, a ping
# from a client program.  It includes artifical lost packets using a random
# number generator that has a chance of losing 3 in 10 packets received.

# The socket module used for network communications
from socket import *
# Used for generating random number for artificial packet loss
import random

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

# Message shows the server process is running
print("Waiting for Client....\n")

# Incoming ping message counter
pingNum = 0

while True:
    # Increment ping counter
    pingNum += 1

    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)

    # Receive the client packet (a ping message)
    message, address = serverSocket.recvfrom(1024)

    # If rand is less than 4, and this is not the first "ping" of
    # a group of 10, consider the packet lost and do not respond
    if rand < 4 and pingNum % 10 != 1:
        print("\nPacket was lost.\n\n")
        continue

    # Otherwise, the server responds
    print("PING {} Received".format(pingNum))
    print("Mesg rcvd: {}".format(message.decode()))
    replyMessage = message.decode().upper()
    serverSocket.sendto(replyMessage.encode(), address)
    print("Mesg sent: {}\n".format(replyMessage))
