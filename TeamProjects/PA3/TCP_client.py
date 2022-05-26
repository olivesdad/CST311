from concurrent.futures import thread
from socket import *
import threading

tLock = threading.Lock()
serverName = "127.0.0.1"
serverPort = 12000

def threadListener(sock, connected):
    #loop for reading and printing messages
    sock.settimeout(1)
    while connected[0]:
        try:
            message = sock.recv(1024).decode()
        except:
            continue
        if message.strip().lower() == 'bye':
            tLock.acquire()
            connected[0]=False
            tLock.release()
            print('Partner said Bye!')
            break
        print('Message: {}'.format(message))
        print('connectin: {}'.format(connected[0]))
    sock.close()
        

def main():

    connected=[True]
    
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    # This bit is for the "client has connected"
    serverResponse = clientSocket.recv(1024)
    print("From Server: " + serverResponse.decode())

    # Wait for ok
    ok = "no"
    while ok != "yes":
        ok = clientSocket.recv(1024).decode()

    #create listener thread
    chatListener = threading.Thread(target=threadListener, args=(clientSocket, connected))
    chatListener.start()
    
    #loop for message sending
    while connected[0]:
        # Here to send the message
        message = input("Enter message to send to server: ")
        #if we send bye then set connected to false
        if message.strip().lower() == 'bye':
            tLock.acquire()
            connected[0] = False
            tLock.release()
        clientSocket.send(message.encode())

    #wait for listener to end then close socket
    print("just watiing for listenetr")
    chatListener.join()
    print('listener closed')
    clientSocket.close()


if __name__ == "__main__":
    main()
