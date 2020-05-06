# -*- coding: utf-8 -*-
"""
@author: Felix
Module that contains Code examples for different Client-Server-Communication methods
"""


############################## PHP ############################################

#Importing Libraries
from urllib.parse import urlencode
from urllib.request import Request, urlopen

#Python function to access a PHP-Script
def httpPost(url, params):	#Paramsformat = {'foo':'bar'}
    request = Request(url, urlencode(params).encode())
    data = urlopen(request).read().decode('utf8') 
    return data


#Declaring the root-URL
root = 'http://feriedel.esy.es/intp/'
script = 'post_test.php'
parameters = {'test_wert':'1'}

contacts = httpPost(root + script, parameters)

###############################################################################

########################### TCP/IP ############################################

############Server#######################

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "192.168.1.4"	#Server IP
port = 1234	#Server Port
address = (ip, port)
server.bind(address)
server.listen(100) #Number of clients that can be connected to the server simultaneously
print("[*] Started listening on ", ip, ":",port)
client, addr = server.accept()
print ("[*] Got a connection from ", addr[0], ":", addr[1])


############Client#######################

import socket

ip = '192.168.1.110'	#Server IP
port = 1234	#Server Port
address = (ip, port)
client = socket.socket()
client.connect(address)
