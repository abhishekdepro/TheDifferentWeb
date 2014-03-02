"""This is the basic directed graph datastructure implementation of the peer
network. This is particularly useful to construct Graphs and Trees of the
available list of peers.

ex: peerlist=['France','Italy','Greece','belgium']
    France--(2)-->Italy--(-1)-->Greece--(4)-->Belgium
    where (2),(-1) are weights between the nodes. or the edges between nodes.

Considering nodes,edges as (v,e) we use networkx library of Python to implement
single-source shortest path algorithm (Bellman-Ford Algo).
"""

#author: Abhishek Dey
#version: 1.0.0
#date: 2nd Mar, 2014

#import networkx library available at https://pypi.python.org/pypi/networkx/
#To install the library/module simply use: pip install networkx
#we import networkx as nx as its easy to write nx everytime we call it.

import networkx as nx


graph=nx.Graph()             #form a basic Graph structure with 0 nodes.
digraph=nx.DiGraph(graph)    #creates a directed graph

#function to add nodes to the directed graph using a list of peers
def add_nodes_to_digraph(nodes):
    digraph.add_nodes_from(nodes)#add nodes from list of nodes
    print digraph.nodes()        #test using print if nodes are added.
    return digraph

#function to add edges for (u,v) in nodes with weights
#weightedgelist should be of form [(source,destination,weight),(..),(..)]
"""
ex: nodes=[1,2,3]

    1--(-1)-->2--(2)-->3--(4)-->2
    |                  ^
    |____(3)___________|

    weightedgelist=[(1,2,-1),(1,3,3),(2,3,2),(3,2,4)]
    where () are tuples. Why?!! Think about it! :)

    Implementation:

    >>> weights=[(1,2,-1),(1,3,3),(2,3,2),(3,2,4)]
    >>> digraph=G.add_edges_to_digraph(weights)
    [(1, 2), (1, 3), (2, 3), (3, 2)]
    >>> G.print_node_edge_data(digraph)
    #Source----Destination---weight#
    1--->2 : {'weight': -1}
    3--->2 : {'weight': 4}
    1--->3 : {'weight': 3}
    2--->3 : {'weight': 2}
    
"""
def add_edges_to_digraph(weightedgelist):
    digraph.add_weighted_edges_from(weightedgelist)
    print digraph.edges()
    return digraph

def print_node_edge_data(DG):
    print '#Source----Destination---weight#'
    if(nx.is_directed(DG)):
        for node in DG.nodes_iter():
            for item in DG.adjacency_iter():
                    if item[1].has_key(node):
                            print str(item[0])+'--->'+str(node)+' : '+str(item[1][node])
    else:
        print 'Not a Directed Graph'


"""
NETWORKX LICENSE:

Copyright (C) 2004-2012, NetworkX Developers
Aric Hagberg <hagberg@lanl.gov>
Dan Schult <dschult@colgate.edu>
Pieter Swart <swart@lanl.gov>
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:
*
Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
*
Redistributions in binary form must reproduce the above
copyright notice, this list of conditions and the following
disclaimer in the documentation and/or other materials provided
with the distribution.
*
Neither the name of the NetworkX Developers nor the names of its
contributors may be used to endorse or promote products derived
from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
