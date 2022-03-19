#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 21:41:53 2022

@author: msayed
"""

from socket import *
import threading
import sys
import ast




if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)

    
# The proxy server is listening at 8888 
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind((sys.argv[1], 8888))
tcpSerSock.listen(100)

file = open("log.txt", "r")

contents = file.read()
dictionary = ast.literal_eval(contents)

file.close()


#while 1:
       
# Start receiving data from the client
print('Ready to serve...')
## FILL IN HERE...
conn, addr = tcpSerSock.accept()

print('Received a connection from:', addr)
#while True:
data = conn.recv(1024)
print(data.decode())

first_line = data.split(b'\r\n')[0]

# get url
resource = first_line.split(b' ')[1]

print(resource.decode())
print(resource.decode()[1:])

resource_name = resource.decode()[1:]

link = 'www.' + resource_name

print(link)
#print(type(link))

print(gethostbyname(link))

if resource in dictionary.keys():
    print('Flie exist in cache')
    conn.send(dictionary[resource])
else:
    print('Flie doen not exist in cache')
    

    #try:
    # create a socket to connect to the web server
    s = socket(AF_INET, SOCK_STREAM)
    
    s.connect((link, 80))
    
    req = "GET " + "http://" + resource_name + " HTTP/1.0\n\n"
    
    s.send(str.encode(req)) 
    
    #tempFile = s.makefile('w', 0)
    #tempFile = s.makefile(mode='b')
    #tempFile.write("GET "+"http://" + resource_name + " HTTP/1.0\n\n")
    #s.sendall(data)                   
    
    while 1:
        d = s.recv(1024)   
        #d = tempFile.readline() 
        
        print(d)       
        if (len(d) > 0):
            conn.send(d)
            dictionary[resource] = d
            with open('log.txt','w') as data: 
                data.write(str(dictionary))                   
        else:
            break
    
    s.close()
    conn.close()


"""
except socket.error as error_msg:
    self.log("ERROR", client_addr, error_msg)
    if s:
        s.close()
    if conn:
        conn.close()
    self.log("WARNING", client_addr, "Peer Reset: " + first_line)

#print('Received a connection from:', addr)
"""
#message = ## FILL IN HERE...
#print(message)
# Extract the filename from the given message

## FILL IN HERE...

#filetouse = ## FILL IN HERE...

try:
    # Check wether the file exist in the cache

    ## FILL IN HERE...

    fileExist = "true"
    # ProxyServer finds a cache hit and generates a response message
    #tcpCliSock.send("HTTP/1.0 200 OK\r\n")            
    #tcpCliSock.send("Content-Type:text/html\r\n")


    ## FILL IN HERE...


# Error handling for file not found in cache, need to talk to origin server and get the file
except IOError:
    if fileExist == "false": 
        a = 2
        ## FILL IN HERE...
        #except:
            #print("Illegal request")                                               
    else:
        a = 2
        # HTTP response message for file not found
        #tcpCliSock.send("HTTP/1.0 404 sendErrorErrorError\r\n")                             
        #tcpCliSock.send("Content-Type:text/html\r\n")
        #tcpCliSock.send("\r\n")

# Close the client and the server sockets  
#s.close()
#tcpCliSock.close() 
tcpSerSock.close()