import DHT
import Splitter
from DHT import DistributedHashTable
md5hashstring=''
count=1

md5hashstring=str(Splitter.split())
distribute=DistributedHashTable(md5hashstring)
distribute.tochararray()
print distribute.chararray

distribute.createkeyvaluepairs()
print distribute.pieces

peerlist=[1,2,3,4]


print md5hashstring
