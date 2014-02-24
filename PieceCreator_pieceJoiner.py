#author: zed41
#version: noob
#date: 24.02.14
import hashlib
#hashlib is a collection of hash fucntions
#GlobalVar fileNames as it will me used by two fucntions
fileNames=[]
def split():
    fn=input("Enter the File You Want to Break into Pieces: ")#The File Should be on the same Directory Where the program is
    f=open(fn,'rb')#file opened in readable binary mode.
    data=f.read()#Content of the file is read and stored in data
    f.close()
    fsize=len(data)
    psize=1000#size in bytes of every piece
    
    md5=hashlib.md5(data).hexdigest()#md5checkSum of the file Contents
    print ("This Is the md5 CheckSum Of the File:")
    print (md5)
    for i in range (0,fsize+1,psize):#breaking the file into pieces

        pieces="%spiece"%md5 + "%s.ari"%i
        fileNames.append(pieces)
        f=open(pieces,'wb')
        f.write(data[i:i+psize])
        f.close()
def create():#Create file from Pieces func
    md5=input("Enter md5 CheckSum of the pieces you want to merge: ")
    dataList=[]
    new="merged%s.jpg"%md5#newfile Name
    for fn in fileNames: #contents from every piece is stored into dataList
        if fn[0:32]==md5:#The pieces we created for a particular file is only accessiable by the checksum of the file contetnt
            f=open(fn,'rb')
            dataList.append(f.read())
            f.close()
    f=open(new,'wb') #writing the data in newfile from dataList
    for data in dataList:
        f.write(data)
    f.close()
    
while 1:
    ch=input("MENU 1.SPLIT \n 2.Create \n Choice:")#noob menu :p
    if ch=='1':
        split()
    if ch=='2':
        create()
    
    
 

