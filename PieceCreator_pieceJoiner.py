import hashlib
fileNames=[]
def split():
    fn=input("Enter the File You Want to Break into Pieces: ")
    f=open(fn,'rb')
    data=f.read()
    f.close
    fsize=len(data)
    psize=1000
    
    md5=hashlib.md5(data).hexdigest()
    print ("This Is the md5 CheckSum Of the File:")
    print (md5)
    for i in range (0,fsize+1,psize):

        pieces="%spiece"%md5 + "%s.ari"%i
        fileNames.append(pieces)
        f=open(pieces,'wb')
        f.write(data[i:i+psize])
        f.close()
def create():
    md5=input("Enter md5 CheckSum of the pieces you want to merge: ")
    dataList=[]
    new="merged%s.jpg"%md5
    for fn in fileNames:
        if fn[0:32]==md5:
            f=open(fn,'rb')
            dataList.append(f.read())
            f.close()
    f=open(new,'wb')
    for data in dataList:
        f.write(data)
    f.close()
    
while 1:
    ch=input("MENU 1.SPLIT \n 2.Create \n Choice:")
    if ch=='1':
        split()
    if ch=='2':
        create()
    
    
 

