# import socket programming library
import socket
 
# import thread module
from _thread import *
import threading
print_lock = threading.Lock()

def Main():
    host = ""
 
    # reserve a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 11323
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
 
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    while True:
        ans = input('\nDo you want to connect to client(y/n) :')
        if ans == 'n':
            break
        # establish connection with client
        c, addr = s.accept()
        
        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
        msg = "Hi! this is window-3"
        c.send((msg.encode('ascii')))
        print_lock.release()

    s.close()
 
 
if __name__ == '__main__':
    Main()    