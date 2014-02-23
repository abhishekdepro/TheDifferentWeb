>>> ================================ RESTART ================================
>>> 
>>> party=DistributedHashTable('Kejriwal')
>>> party.tochararray()
['K', 'e', 'j', 'r', 'i', 'w', 'a', 'l']
>>> party.createkeyvaluepairs()
{'1': ['e'], '0': ['K'], '3': ['r'], '2': ['j'], '5': ['w'], '4': ['i'], '7': ['l'], '6': ['a']}
>>> import DHT
>>> pl=[1,2,3,4]

#Iteration 1.
>>> DHT.randomize(pl,party)
Piece 1 sent to 1 : DATA :['e', 1]
Piece 0 sent to 3 : DATA :['K', 3]
Piece 3 sent to 1 : DATA :['r', 1]
Piece 2 sent to 1 : DATA :['j', 1]
Piece 5 sent to 3 : DATA :['w', 3]
Piece 4 sent to 2 : DATA :['i', 2]
Piece 7 sent to 1 : DATA :['l', 1]
Piece 6 sent to 3 : DATA :['a', 3]
>>> DHT.sortbypeers(party)
>>> DHT.displaypeerdatainfo()
Peer no. 1 has data: ['e', 'r', 'j', 'l']
Peer no. 2 has data: ['i']
Peer no. 3 has data: ['K', 'w', 'a']

#Iteration 2
>>> DHT.randomize(pl,party)
Piece 1 sent to 4 : DATA :['e', 1, 4]
Piece 0 sent to 3 : DATA :['K', 3, 3]
Piece 3 sent to 4 : DATA :['r', 1, 4]
Piece 2 sent to 4 : DATA :['j', 1, 4]
Piece 5 sent to 3 : DATA :['w', 3, 3]
Piece 4 sent to 4 : DATA :['i', 2, 4]
Piece 7 sent to 3 : DATA :['l', 1, 3]
Piece 6 sent to 2 : DATA :['a', 3, 2]
>>> DHT.sortbypeers(party)
>>> DHT.displaypeerdatainfo()
Peer no. 1 has data: ['e', 'r', 'j', 'l', 'e', 'r', 'j', 'l']
Peer no. 2 has data: ['i', 'i', 'a']
Peer no. 3 has data: ['K', 'w', 'a', 'K', 'K', 'w', 'w', 'l', 'a']
Peer no. 4 has data: ['e', 'r', 'j', 'i']

#Iteartion 3
>>> DHT.randomize(pl,party)
Piece 1 sent to 4 : DATA :['e', 1, 4, 4]
Piece 0 sent to 2 : DATA :['K', 3, 3, 2]
Piece 3 sent to 4 : DATA :['r', 1, 4, 4]
Piece 2 sent to 3 : DATA :['j', 1, 4, 3]
Piece 5 sent to 1 : DATA :['w', 3, 3, 1]
Piece 4 sent to 2 : DATA :['i', 2, 4, 2]
Piece 7 sent to 1 : DATA :['l', 1, 3, 1]
Piece 6 sent to 2 : DATA :['a', 3, 2, 2]
>>> DHT.sortbypeers(party)
>>> DHT.displaypeerdatainfo()
Peer no. 1 has data: ['e', 'r', 'j', 'l', 'e', 'r', 'j', 'l', 'e', 'r', 'j', 'w', 'l', 'l']
Peer no. 2 has data: ['i', 'i', 'a', 'K', 'i', 'i', 'a', 'a']
Peer no. 3 has data: ['K', 'w', 'a', 'K', 'K', 'w', 'w', 'l', 'a', 'K', 'K', 'j', 'w', 'w', 'l', 'a']
Peer no. 4 has data: ['e', 'r', 'j', 'i', 'e', 'e', 'r', 'r', 'j', 'i']
>>> 