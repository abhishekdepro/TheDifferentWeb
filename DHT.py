"""Implementation of a different kind of Distributed Hash Table"""
#author: Abhishek Dey
#version: 1.0.0
#date: 23rd Feb,2014

import random
pieces={}
peers={}
"""Class DHT to create distributed hash table"""
class DistributedHashTable(object):
    #default constructor used as a String builder
    def __init__(self,string):
        self.string=string
        pieces={}
        chararray=[]
        peers={}
        
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
    
    dist=[]
    for piece in Table.pieces:
        dist=Table.pieces[str(piece)]
        for i in range(1, len(dist)):
            if((peers.has_key(dist[i]))==True):
                peers[dist[i]].append(dist[0])
            else:
                peers[dist[i]]=list(dist[0])

#display peer data list
def displaypeerdatainfo():
    for peer in peers:
        print 'Peer no. '+ str(peer) + ' has data: '+ str(peers[peer])

#check if peer has all pieces
def recvdall(Table,peer):
    if (Table.peers[str(peer)]==Table.chararray):
        print 'Fiesta'


    
