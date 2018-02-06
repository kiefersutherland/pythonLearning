from random import randint
from random import randrange
import json 
import time

ISOTIMEFORMAT='%Y-%m-%d %X'
ctime=time.strftime(ISOTIMEFORMAT, time.localtime())
print(ctime)
t=randrange(0,99)
print(t)

filename='text.txt'
jsonfiLe='test.json'
strFile=[] 
y=0
while y < 1000:
 x = randint(0,6)
 strFile.append(str(x)) 
 y=y+1 

with open(filename,'w') as fileObject:
    fileObject.write(str(strFile)) 


with open(jsonfiLe,'w') as jsonObj:
    json.dump(strFile,jsonObj)  

print("写入文本")
ctime=time.strftime(ISOTIMEFORMAT, time.localtime())
print(ctime)
 