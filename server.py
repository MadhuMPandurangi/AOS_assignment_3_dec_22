# # import socket programming library
# import socket
 
# # import thread module
# from _thread import *
# import threading


# # win = [0,0,0]
# token = 0
# print_lock = threading.Lock()

# # def window_1(token):

# # def window_2(token):


# # def window_3(token):



# # def redirect_client_thread(token):
# #     if token%3 == 1:
# #         w1 = threading.Thread(target=window_1, args=(token, ))
# #         w1.start()
# #     elif token%3 == 2:
# #         w2 = threading.Thread(target=window_2, args=(token, ))
# #         w2.start()
# #     elif token%3 == 0:
# #         w3 = threading.Thread(target=window_3, args=(token, ))  
# #         w3.start()
# #     return       
 
# # thread function
# def threaded(c):

#     global token
#     # data received from client
#     #data = c.recv(1024)
    

#     # reverse the given string from client
#     #data = data[::-1]
#     token = token + 1
#     if(token<5):
#         c.send(str(token).encode('ascii'))    
#         # send back reversed string to client
        
#         print_lock.release()

#         # t1 = threading.Thread(target=redirect_client_thread, args=(token, ))
#         # t1.start()
#         # connection closed
#         c.close()
#     else:
#         print_lock.release()
#     c.close()    
        
    
 
 
# def Main():
#     host = ""
 
#     # reserve a port on your computer
#     # in our case it is 12345 but it
#     # can be anything
#     port = 12345
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind((host, port))
#     print("socket binded to port", port)
 
#     # put the socket into listening mode
#     s.listen(5)
#     print("socket is listening")
    
#     global token
#     # a forever loop until client wants to exit

#     while(token < 4):
#         # ans = input('\nDo you want to connect to client(y/n) :')
#         # if ans == 'n':
#         #     break
#         # establish connection with client
#         c, addr = s.accept()
        
#         # lock acquired by client
#         print_lock.acquire()
#         print('Connected to :', addr[0], ':', addr[1])
        
        
#         # Start a new thread and return its identifier
#         start_new_thread(threaded, (c,))
        
        
        
#     s.close()
 
 
# if __name__ == '__main__':
#     Main()






























# import socket programming library
import socket
 
# import thread module
from _thread import *
import threading


# win = [0,0,0]
token = 0
print_lock = threading.Lock()

# def window_1(token):

# def window_2(token):


# def window_3(token):



# def redirect_client_thread(token):
#     if token%3 == 1:
#         w1 = threading.Thread(target=window_1, args=(token, ))
#         w1.start()
#     elif token%3 == 2:
#         w2 = threading.Thread(target=window_2, args=(token, ))
#         w2.start()
#     elif token%3 == 0:
#         w3 = threading.Thread(target=window_3, args=(token, ))  
#         w3.start()
#     return       
 
# thread function
def threaded(c):

    global token
    # data received from client
    #data = c.recv(1024)
    

    # reverse the given string from client
    #data = data[::-1]
    token = token + 1
    if(token<5):
        c.send(str(token).encode('ascii'))    
        # send back reversed string to client
        
        print_lock.release()

        # t1 = threading.Thread(target=redirect_client_thread, args=(token, ))
        # t1.start()
        # connection closed
        c.close()
    else:
        print_lock.release()
    c.close()    
        
    
 
 
def Main():
    host = ""
 
    # reserve a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12344
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
 
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")
    
    global token
    # a forever loop until client wants to exit

    while(token < 4):
        # ans = input('\nDo you want to connect to client(y/n) :')
        # if ans == 'n':
        #     break
        # establish connection with client
        c, addr = s.accept()
        
        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
        
        
        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
        
        
        
    s.close()
 
 
if __name__ == '__main__':
    Main()