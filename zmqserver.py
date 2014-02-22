"""This file creates a message passing server"""
"""This will be installed on all the peers that shall host the files"""
"""Extensive Documentation using zmq at:http://learning-0mq-with-pyzmq.readthedocs.org/en/latest/pyzmq/patterns/patterns.html"""
#author: Abhishek Dey
#version: 1.0.0
#date: 22nd Feb, 2014.

import zmq
import time
import sys

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.REP)  #for server we use REP
socket.bind("tcp://*:%s" % port)


while True:
    #  Wait for next request from client
    message = socket.recv()
    print "Received request: ", message
    time.sleep (1)  
    socket.send("World from %s" % port)