import threading
from socket import *

lock = threading.Lock()

# Use this class for shared variables
class SharedData:
    def __init__(self):
        self.order = []
        self.messages = {"X": "", "Y": ""}
        self.bufferFull = {"X": False, "Y": False}
        self.connected = {"X": False, "Y": False}

    def hasMessage(self, client):
        return self.bufferFull[client]

    def getMessage(self, client):
        return self.messages[client]


# This function used to create the thread connections
def connect(name, socket, data):
    ready = False
    # Just output to tell what client you are and show in server instance
    if name == "X":
        print("Accepted first connection, calling it client X")
        socket.send("Client X connected\n".encode())
    elif name == "Y":
        print("Accepted second connection, calling it client Y")
        socket.send("Client Y Connected\n".encode())
    else:
        print("unknown client error")

    #Set ourselves as connected
    data.connected[name]=True
    # Wait for both clients to connect
    connected = False
    while not connected:
        if data.connected["X"] and data.connected["Y"]:
            connected = True

    # both connected now send ok
    print("SENDING OK")
    socket.send("yes".encode())
    # wait for data from client
    message = socket.recv(1024).decode()

    # Lock data and set message also append your name to the order
    lock.acquire()
    data.bufferFull[name] = True
    data.messages[name] = message
    data.order.append(name)
    lock.release()

    # wait for both clients to send
    while not ready:
        ready = data.bufferFull["Y"] if name == "X" else data.bufferFull["X"]

    # This is kind of hacky use the order of the 'order' list to determine who sent first
    first = data.order[0]
    second = data.order[1]
    results = "{}: {} recieved before {}: {}".format(
        first, data.messages[first], second, data.messages[second]
    )
    socket.send(results.encode())
    socket.close()


def Main():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # this line I guess sets the timeout to instant after socket closed
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(("", serverPort))
    serverSocket.listen(1)

    clients = 1
    threads = ["", ""]
    names = ["X", "Y"]

    # instantiate the messages shared data object
    messages = SharedData()

    print("The server is waiting to receive 2 connections...")

    # Create 2 threads
    while clients <= 2:
        connectionSocket, addr = serverSocket.accept()

        # create a connection (thread) put it in the list then start it
        threads[clients - 1] = threading.Thread(
            target=connect, args=(names[clients - 1], connectionSocket, messages)
        )
        threads[clients - 1].start()
        clients += 1

    # wait here for the threads to complete
    for thread in threads:
        thread.join()
    serverSocket.close()

    print("main done")


if __name__ == "__main__":
    Main()
