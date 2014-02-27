"""Peering information and forming the peer information table"""
#author: Abhishek Dey
#version: 1.0.0
#date: 27th Feb, 2014



class PeerInfo:
    #initialize peering information for this class
    
    def __init__(self,peerlist):
        if (type(peerlist)==list):
            self.peers=peerlist
        else:
            self.peers=list(peerlist)
            peers=self.peers
        for peer in self.peers:
            self.setpeerattributes(peer)

    #used as a setter method for key attributes of a peer
    def setpeerattributes(self,peer):
        self.peer_id=peer[0][0]     #These are as of now, suggest modifications
        self.peer_ip=peer[1]
        self.peer_port=peer[2]
        self.peer_uploaded=peer[3]
        self.peer_download=peer[4]
        self.peer_remaining=peer[5]

    #returns attributes for peer
    def getpeerattribute(self,peer_no,attrib):
        if attrib=='peer_id':
            return self.peers[peer_no].peer_id
        elif attrib==peer_ip:
            return self.peer_ip
        elif attrib==peer_port:
            return self.peer_port
        elif attrib==peer_uploaded:
            return self.peer_uploaded
        elif attrib==peer_downloaded:
            return self.peer_downloaded
        elif attrib==peer_remaining:
            return self.peer_remaining

    
    
                
        
