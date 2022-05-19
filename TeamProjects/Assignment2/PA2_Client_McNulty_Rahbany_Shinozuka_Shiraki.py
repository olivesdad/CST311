# Names: Juli Shinozuka, Nadia Rahbany, Kevin McNulty, Andrew Shiraki
# Date: May 16, 2022
# Description: This is a client program that pings a UDP server for
# a response.  Calcuations are done each ping-pong and a summary at
# the end about the process' round-trip time (RTT).

# The socket module used for network communications
from socket import *
# Used for calculating elapsed time
from time import time

serverName = '127.0.0.1'    # The ip address of server
serverPort = 12000          # The server port to be used

# Used for ping counting and calculation
MAX_PINGS = 10
pingNum = 0
receivedPingReplies = 0

# used for summary calculations (in seconds where time is used)
pongRTT = 0             # The SampleRTT to calc estimatedRTT and devRTT
minRTT = 0
maxRTT = 0
avgRTT = 0
packetLoss = 0.0        # 0.60 means 60% packet loss
estimatedRTT = 0
devRTT = 0
timeoutInterval = 0
totalElapsedTime = 0    # The totalRTT to calc avgRTT
alpha = 0.125           # Used in calculating estimatedRTT (0.125 recommended)
beta = 0.25             # Used in calculating devRTT (0.25 recommended)

# create UDP socket with 1 second timeout
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(0,MAX_PINGS):  
    # Increatement ping counter
    pingNum += 1
    # Set ping message variable (will be sent to server)
    message = "Ping" + str(pingNum)

    try:
        # Send ping message to server (start timer)
        startTime = time()
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        print("Mesg sent: {}".format(message))

        # Receive reply message from server (stop timer and update counter)
        replyMessage, serverAddress = clientSocket.recvfrom(1024)
        returnTime = time()
        print("Mesg rcvd: {}".format(replyMessage.decode()))
        receivedPingReplies += 1

        # Display ping transmission stats (time output in ms)
        pongRTT = returnTime - startTime
        print("Start time: {}".format(startTime))
        print("Return time: {}".format(returnTime))
        print("PONG {} RTT: {} ms\n".format(pingNum, (pongRTT * 1000)))

        # Check minRTT and maxRTT
        # If minRTT or maxRTT is 0, then initialize values with current pongRTT
        if((pongRTT < minRTT) or (minRTT == 0)):
            minRTT = pongRTT
        if((pongRTT > maxRTT) or (maxRTT == 0)):
            maxRTT = pongRTT

        # Calculate estimatedRTT and devRTT (only for responses)
        # First ping always succeeds (in this senario)
        if(pingNum == 1):
            estimatedRTT = pongRTT
            devRTT = pongRTT / 2
        else:
            estimatedRTT = ((1 - alpha) * estimatedRTT) + (alpha * pongRTT)
            devRTT = ((1 - beta) * devRTT) + (beta * abs(pongRTT - estimatedRTT))

        # Calculate Total Elapsed Time
        totalElapsedTime += pongRTT

    except timeout:
        print("No Mesg rcvd")
        print("PONG {} Request Timed out\n".format(pingNum))

# closes the socket.  end of process.
clientSocket.close()

# Calculations for summary (in seconds)
avgRTT = totalElapsedTime / receivedPingReplies
timeoutInterval = estimatedRTT + (4 * devRTT)
packetLoss = (MAX_PINGS - receivedPingReplies)/MAX_PINGS

# Display summary (multipled by 1000 to get ms since time variables are in seconds)
print("Min RTT:           {} ms".format(minRTT * 1000))
print("Max RTT:           {} ms".format(maxRTT * 1000))
print("Avg RTT:           {} ms".format(avgRTT * 1000))
print("Packet Loss:       {} % ".format(packetLoss * 100))
print("Estimated RTT:     {} ms".format(estimatedRTT * 1000))
print("Dev RTT:           {} ms".format(devRTT * 1000))
print("Timeout Interval:  {} ms".format(timeoutInterval * 1000))
