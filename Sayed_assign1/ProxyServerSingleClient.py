#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 05:15:49 2022

@author: msayed
"""

from socket import *
import threading
import sys
import ast
import signal

# Global variable, 
dictionary = {}

def proxy_handler(tcpCliSock, addr):
    """
    This function acts as a proxy server which will handle particular client request(browser). Main purpose of
    this function is to provide multithreading. Server actually hand over every cleint connection to this 
    function and will wait for new client request.
    
    Arguments:
    tcpCliSock -- TCP client socket after connected
    addr -- IP adress and port
    
    Returns:
    None.
    """
    global dictionary
    
    # Received request from client
    message = tcpCliSock.recv(1024)

    # Print client request and decode it because it's byte.
    print('Client Request : ', message.decode())

    ### Find out resource name ###

    # First split whole http request by '\r\n' and only consider first line which has GET as 
    # GET request has resouce name in it.
    first_line = message.split(b'\r\n')[0]

    # Split first line by ' ' and consider second element which is nothing but resource name.
    resource = first_line.split(b' ')[1]

    # Print resource name 
    print('Resource wanted by client : ', resource.decode())

    # Print resource name without initial '/' 
    print('Resource wanted by client(without slash) : ', resource.decode()[1:])

    # Erase initial '/' in resource name
    resource_name = resource.decode()[1:]

    # Make link by adding 'www.' prefix with resource_name
    link = 'www.' + resource_name


    # Print IP adress of the domain
    print('Domain, IP Address : ', link, gethostbyname(link))

    # Check resource request is resolved at proxy server? 
    
    
    # First check wheather cache hit or miss happen?
    hit = True if resource in dictionary.keys() else False
    
    # Cache hit happens
    if hit:
        print('File exists in cache.')
        
        # Send a cached copy to client browser.
        tcpCliSock.send(dictionary[resource])
        print('Resource sended to client browser.')
        
        
        
    # Resource request is not resolved at proxy server.
    # Cache miss happens
    else:
        print('Flie does not exist in cache.')
        
        try:
            # Create a socket to connect to the web server.
            tcpWebSerSock = socket(AF_INET, SOCK_STREAM)
            tcpWebSerSock.connect((link, 80))
            
            print('Connection established with web server.')
            
            # HTTP get request for getting resource from webserver 
            req = "GET " + "http://" + resource_name + " HTTP/1.0\n\n"
            
            
            # Send HTTP request to webserver.
            tcpWebSerSock.send(str.encode(req)) 
            
            
            # Try to use socket.makefile, but not working gave some errors.
            #tempFile = s.makefile('w', 0)
            #tempFile = s.makefile(mode='b')
            #tempFile.write("GET "+"http://" + resource_name + " HTTP/1.0\n\n")
            #s.sendall(data)                   
            
            while True:
                # Receive Http response from web server. 
                http_response = tcpWebSerSock.recv(1024)   
                #msg = tempFile.readline() 
                print('Http response received from web server.')
                
                # Print http response.
                print('Http response from webserver: ', http_response.decode())       
                if (len(http_response) > 0):
                    # Send http response back to client's web browser.
                    tcpCliSock.send(http_response)
                    print('Http response send to client browser.')
                    
                    
                    # Store http response info of the resource in dictionary.
                    dictionary[resource] = http_response
                    
                    # Save this resource, response mapping to log file.
                    with open('log.txt','w') as data: 
                        data.write(str(dictionary))  
                        
                else:
                    break
            
            # Close websocket
            tcpWebSerSock.close()
            
            
        except tcpWebSerSock.error as error:
            print("Caught exception tcpWebSerSock.error : %s", error)
        except tcpCliSock.error as error:
            print("Caught exception tcpCliSock.error : %s", error)
            
    try:  
        # Close the client sockets 
        tcpCliSock.close()
    except tcpCliSock.error as error:
        print("Caught exception tcpCliSock.error : %s", error)
    

def main():
    """
    Open servver socket and bind it at localhost and port 8888. Load cache from log.txt and store it in python dictionary.
    Receiving cleint request and dispatch it to proxy thread.
    
    Arguments:
    None.
    
    Returns:
    None.
    """
    global dictionary

    if len(sys.argv) <= 1:
        print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
        sys.exit(2)
    
    # Open log file(stored webpage information) and load this data into python dictionary
    file = open("log.txt", "r")
    
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    
    file.close()
    
    try: 
        # The proxy server is listening at 8888 
        tcpSerSock = socket(AF_INET, SOCK_STREAM)
        tcpSerSock.bind((sys.argv[1], 8888))
        tcpSerSock.listen(100)
    except tcpSerSock.error as error:
        print("Caught exception tcpSerSock.error : %s", error)
        
    
       
    # Start receiving data from the client
    print('Ready to serve...')
    
    try:
        # Waiting for client to connect
        tcpCliSock, addr = tcpSerSock.accept()
        
    except tcpSerSock.error as error:
        print("Caught exception tcpSerSock.error : %s", error)
    
    print('Received a connection from:', addr)
    
    # Dispatching client request(browser) to proxy server.
    proxy_handler(tcpCliSock, addr)

    try:  
        # Close the server sockets  
        tcpSerSock.close()
        
    except tcpSerSock.error as error:
        print("Caught exception tcpSerSock.error : %s", error)
    
if __name__ == '__main__':
    main()
    
    
    