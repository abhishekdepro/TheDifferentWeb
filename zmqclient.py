"""This file creates a message passing client"""
"""This will be installed on all the server hosting the DHT to be notified about change in files by peers"""
#author: Abhishek Dey
#version: 1.0.0
#date: 22nd Feb, 2014.

import zmq
import sys

port = "5556" #can be anything as well
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ) #for client we use REQ
socket.connect ("udp://localhost:%s" % port)
if len(sys.argv) > 2:
    socket.connect ("udp://localhost:%s" % port1)


#  Do 10 requests, waiting each time for a response
for request in range (1,10):
    print "Sending request ", request,"..."
    socket.send ("Hello")
    #  Get the reply.
    message = socket.recv()
    print "Received reply ", request, "[", message, "]"

