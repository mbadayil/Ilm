import os
import time
import hashlib

#print(os.listdir('/Users/adam/Desktop/Atom'))


checkList={}
duplicate={}
def checkSum(fname, chunk_size=1024):
    hash=hashlib.md5()
    with open(fname, "rb") as f1:
        chunk=f1.read(chunk_size)
        hash.update(chunk)
        f1.read(chunk_size)

    return hash.hexdigest()



for dirpath,dirname,files in os.walk('/Users/adam/Desktop/Atom'):
    for file in files:
        file=os.path.join(dirpath,file)
        #file=file.encode('utf-8')
        checksum1=checkSum(file)
        if checksum1 not in checkList.values():
            checkList.update({file:checksum1})
        else:
            for key, value in checkList.items():
                if value==checksum1:
                    pytime = time.ctime((os.path.getmtime(key)))
                    newtime = time.ctime((os.path.getmtime(file)))
                    if pytime<newtime:
                        duplicate.update({file:newtime})
                        #print(file, newtime)
                    else:
                        duplicate.update({key:pytime})
                        #print(key, pytime)

print(duplicate)
