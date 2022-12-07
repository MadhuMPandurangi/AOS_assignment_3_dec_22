# # Import socket module
# import socket
# import datetime
 
# def connect_win(token):
#     # connecting with windows

#     if int(token)%3 == 1:
#         host = '127.0.0.1'
#         port = 11123
#     elif int(token)%3 == 2:
#         host = '127.0.0.1'
#         port = 11223
#     elif int(token)%3 == 0:
#         host = '127.0.0.1'
#         port = 11323        
 
#     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
#     # connect to server on local computer
#     s.connect((host,port))

#     data = s.recv(1024)
#     if data:
#         print('Window response: ',str(data.decode('ascii')))    
#         print('vaccinated at: ', str(datetime.datetime.now()))
#     s.close()
#     return



# def Main():
#     # local host IP '127.0.0.1'
#     host = '127.0.0.1'
 
#     # Define the port on which you want to connect
#     port = 12345
 
#     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
#     # connect to server on local computer
#     s.connect((host,port))
 
#     # message you send to server
# #message = "shaurya says geeksforgeeks"

#     # message sent to server
#     #s.send(message.encode('ascii'))

#     # message received from server
#     token = s.recv(1024)
#     # print the received message
#     # here it would be a reverse of sent message
#     if not token:
#         print('Token number exceeded')
#         s.close()
#     else:
#         print('Your token number is :',str(token.decode('ascii')))
#         connect_win(token)
    
    

#     # ask the client whether he wants to continue
    
#     # close the connection
#     s.close()



    
 
# if __name__ == '__main__':
#     Main()



























# Import socket module
import socket
import datetime
import time
import json
 
def connect_win(token):
    # connecting with windows

    # if int(token)%3 == 1:
    #     host = '127.0.0.1'
    #     port = 11123
    # elif int(token)%3 == 2:
    #     host = '127.0.0.1'
    #     port = 11223
    # elif int(token)%3 == 0:
    #     host = '127.0.0.1'
    #     port = 11323    
    # f = open('win.json')
    # data = json.load(f)
    # f.close()

    while True:
        f = open('win.json')
        data = json.load(f)
        f.close()   
        if data["win1"] == "0":
            host = '127.0.0.1'
            port = 11123
            data["win1"] = "1"
            flag = 0
            break
        elif data["win2"] == "0":
            host = '127.0.0.1'
            port = 11223
            data["win2"] = "1"
            flag = 1
            break
        elif data["win3"] == "0":
            host = '127.0.0.1'
            port = 11323
            data["win3"] = "1"
            flag = 2
            break
        time.sleep(3)
        

    f = open('win.json','w')
    f.write(json.dumps(data))
    f.close()

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
    # connect to server on local computer
    s.connect((host,port))

    data1 = s.recv(1024)
    if data1:
        print('Window response: ',str(data1.decode('ascii')))    
        print('vaccinated at: ', str(datetime.datetime.now()))

        f = open('win.json')
        data = json.load(f) 
        f.close()
        if(flag == 0):
            data["win1"] = "0"
        elif(flag == 1):
            data["win2"] = "0"
        elif(flag == 2):
            data["win3"] = "0" 

        f = open('win.json','w')
        f.write(json.dumps(data))
        f.close()    

    s.close()
    return



def Main():
    # local host IP '127.0.0.1'
    host = '127.0.0.1'
 
    # Define the port on which you want to connect
    port = 12344
 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
    # connect to server on local computer
    s.connect((host,port))
 
    # message you send to server
#message = "shaurya says geeksforgeeks"

    # message sent to server
    #s.send(message.encode('ascii'))

    # message received from server
    token = s.recv(1024)
    # print the received message
    # here it would be a reverse of sent message
    if not token:
        print('Token number exceeded')
        s.close()
    else:
        print('Your token number is :',str(token.decode('ascii')))
        s.close()
        connect_win(token)
    
    

    # ask the client whether he wants to continue
    
    # close the connection
    # s.close()



    
 
if __name__ == '__main__':
    Main()