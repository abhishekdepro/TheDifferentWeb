"""Implementation of a different kind of Distributed Hash Table"""
#author: Abhishek Dey
#version: 1.0.0
#date: 23rd Feb,2014

pieces={}
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
