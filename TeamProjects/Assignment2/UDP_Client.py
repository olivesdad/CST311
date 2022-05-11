from email import message
from socket import *
import time
import sys

#retrund start end time and add to rtt accumulator 
def timeDiff(start, end, acc):
    diff = round(end * 1000 - start * 1000, 2)
    acc[0]+= diff
    return diff

#call at the end to print results of ping test
def printSummary(hit, pings, rtt):
    loss = ((pings - hit) / pings)*100 
    rttAvg = rtt / hit
    print(f'\nRESULTS: \n'
          f'Attempts:    {pings}\n'
          f'Responsees:  {hit}\n'
          f'Loss rate:   {round(loss,2)}%\n'
          f'Average RTT: {round(rttAvg,2)}ms')

#ping loop
def pingaroo(ip, port):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    pings = 10
    count = 0
    acc = [0.0]
    hit = 0

    while count < pings:
        #try block, get a time stamp, send message wait for response, print response increment hit counter
        try:
            start = time.perf_counter()
            clientSocket.sendto('s'.encode(), (ip, port))
            modMess, serverAddress = clientSocket.recvfrom(2048)
            print(f"PING {ip} time={timeDiff(start, time.perf_counter(), acc)}ms") 
            hit += 1
        
        #socket throws timeout exception so if we exceet timeout go here and just print timeout
        except timeout:
            print('timeout')
            
        count +=1

    #do the summary thing
    printSummary(hit , count, round(acc[0],2) )
    clientSocket.close()

if __name__ == '__main__':
    pingaroo(sys.argv[1], int(sys.argv[2]))


