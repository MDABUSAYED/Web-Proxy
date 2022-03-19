#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:26:17 2022

@author: msayed
"""

from socket import *
import threading
import sys


def proxy(conn, addr):
    data = conn.recv(1024)
    print(data.decode())

    first_line = data.split(b'\r\n')[0]

    # get url
    resource = first_line.split(b' ')[1]

    print(resource.decode())
    print(resource.decode()[1:])

    resource = resource.decode()[1:]

    link = 'www.' + resource

    print(link)
    #print(type(link))

    print(gethostbyname(link))

    #try:
    # create a socket to connect to the web server
    s = socket(AF_INET, SOCK_STREAM)

    s.connect((link, 80))

    req = "GET " + "http://" + resource + " HTTP/1.0\n\n"

    s.send(str.encode(req)) 
    #s.sendall(data)                   

    while 1:
        d = s.recv(1024)          
        if (len(d) > 0):
            conn.send(d)                   
        else:
            break

    s.close()
    conn.close()

if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)

    
# The proxy server is listening at 8888 
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind((sys.argv[1], 8888))
tcpSerSock.listen(100)


while 1:
       
    # Start receiving data from the client
    print('Ready to serve...')
    ## FILL IN HERE...
    conn, addr = tcpSerSock.accept()
    
    print('Received a connection from:', addr)
    #while True:
    d = threading.Thread( target=proxy, args=(conn, addr))
    
    d.setDaemon(True)
    d.start()




tcpSerSock.close()



