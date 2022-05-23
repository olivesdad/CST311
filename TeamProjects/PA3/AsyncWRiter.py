import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out=out

    def run(self):
        f = open(self.out, 'a')
        f.write(self.text + '\n')
        f.close
        time.sleep(2)
        print('finished Background file write')

def MAIN():
    message = input("message: ")
    background = AsyncWrite(message, 'out.txt')
    background.start()
    print(f'the program can continue while it writes in another thread\n')
    print ('100 +400 =', 100+400)
    background.join()
    print('thread complete')

if __name__ == '__main__':
    MAIN()