import DHT
import Splitter
from DHT import DistributedHashTable
md5hashstring=''
count=1

md5hashstring=str(Splitter.split())
hashlist=list(md5hashstring)
hashlist.sort()
#md5hashstring sorted back to a string
md5hashcheck=''.join(hashlist)
distribute=DistributedHashTable(md5hashstring)
distribute.tochararray()
print distribute.chararray

distribute.createkeyvaluepairs()
print distribute.pieces

peerlist=[1,2,3,4,5,6,7]
while (count<=100):
    DHT.randomize(peerlist,distribute)
    DHT.sortbypeers(distribute)

    DHT.displaypeerdatainfo()
    DHT.testmd5(md5hashcheck)
    count=count+1

print md5hashstring
