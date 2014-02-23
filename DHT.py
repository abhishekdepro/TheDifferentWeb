"""Implementation of a different kind of Distributed Hash Table"""
#author: Abhishek Dey
#version: 1.0.0
#date: 23rd Feb,2014

import random
pieces={}

"""Class DHT to create distributed hash table"""
class DistributedHashTable(object):
    #default constructor used as a String builder
    def __init__(self,string):
        self.string=string
        pieces={}
        chararray=[]
        
        
    #slice string to character array
    def tochararray(self):
        self.chararray=list(self.string)
        return self.chararray

    #create a hash table/dictionary
    def createkeyvaluepairs(self):
        for piece in range(0, len(self.chararray)):
            pieces[str(piece)]=list(self.chararray[piece])

        self.pieces=pieces
        return self.pieces



#randomize the pieces to peer list
def randomize(peer_list,Table):
    if type(peer_list) == list:
        for piece in Table.pieces:
            item=random.randint(1,len(peer_list))
            Table.pieces[str(piece)].append(item)
            print 'Piece ' + str(piece) + ' sent to ' + str(item) + ' : DATA :' + str(Table.pieces.get(str(piece)))

#used to see which bits have gone to which peer
def sortbypeers(Table):
    peers={}
    for piece in Table.pieces:
        item=Table.pieces.get(str(piece))
        if((peers.has_key(str(item[1])))==True):
            peers[str(item[1])].append(item[0])
        else:
            peers[str(item[1])]=list(item[0])
    
    print '<---PEER AND FILE INFORMATION--->'
    for peer in peers:
        print str(peer)+ '-->' +str(peers[str(peer)])


    
