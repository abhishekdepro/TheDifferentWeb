fn="FileName.Ext"
f = open(fn, 'rb')
data = f.read()
f.close()
fsize = len(data)
pcsize = 1000
fileNames = []
for i in range(0, fsize+1, pcsize):
    fn1 = "file%s" % i
    fileNames.append(fn1)
    f = open(fn1, 'wb')
    f.write(data[i:i+pcsize])
    f.close()
 
print (int(fsize/pcsize)+1,"No of Pieces created! ^_^")
