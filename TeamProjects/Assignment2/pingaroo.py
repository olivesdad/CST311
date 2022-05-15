from decimal import DivisionByZero
from email import message
from socket import *
import time
import sys
timeouts = 1
numPings = 10

#retrund start end time and add to rtt accumulator 
def timeDiff(start, end, rtts):
    diff = round(end * 1000 - start * 1000, 4)
    rtts.append(diff)
    return diff

#call at the end to print results of ping test
def printSummary(pings, rtts):
    try:
        loss = (int(pings) - len(rtts)) / int(pings) *100
        print(f"pings: {pings} len: {len(rtts)} loss {loss}")
        min= timeouts * 1000
        max = 0
        sum = 0
        hit = len(rtts)

        for num in rtts:
            if num < min:
                min = num
            elif num > max:
                max = num
            sum += num
        
        rttAvg = sum / hit
        print('\nRESULTS: \n'
              'Attempts:    '+str(pings)+'\n'
              'Responsees:  '+str(hit)+'\n'
              'Loss rate:   '+str(round(loss,4))+'%\n'
              'Min rtt:     '+str(min)+'ms\n'
              'Max rtt:     '+str(max)+'ms\n'
              'Average RTT: '+str(round(rttAvg,4))+'ms')
    except ZeroDivisionError:
        print("NO RESPONSE!")

#ping loop
def pingaroo(ip, port, pings):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(timeouts)
    count = 0
    rtts = []
    
    print('Ping to: '+ str(ip)+':'+str(port)+' Count: '+ str(pings))

    while count < pings:
        #try block, get a time stamp, send message wait for response, print response increment hit counter
        try:
            start = time.perf_counter()
            clientSocket.sendto('s'.encode(), (ip, port))
            modMess, serverAddress = clientSocket.recvfrom(2048)
            print("PING "+ str(ip)+" time=" + str(timeDiff(start, time.perf_counter(), rtts)) + "ms") 
    
        
        #socket throws timeout exception so if we exceet timeout go here and just print timeout
        except timeout:
            print('timeout')
            
        count +=1

    #do the summary thing
    printSummary(count, rtts) 
    clientSocket.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: \n python pingaroo <ip> <port>')
        quit()
    pingaroo(sys.argv[1], int(sys.argv[2]), numPings)


