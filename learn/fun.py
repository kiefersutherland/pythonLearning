#import antigravity

''' import __hello__
import this '''
 

import numpy
 

sequare=[v**2 for v in range(1,21)]
print(sequare[2:10])
print(sequare[2:])
print(sequare[-2:])

                                                                                                     
myfood=['鸡','鱼']
friendFood=myfood
herfood=myfood[:]
myfood.append('猪')
friendFood.append('牛')
herfood.append('飞机')
print(myfood)
print(friendFood)
print(herfood)

for f in herfood:
 if f=='飞机':
  print("打"+f)
 else:
     print('吃'+f)

if '飞机' in herfood:
 print('c')

alient_0={}
alient_0["color"]='green'
alient_0["size"]='big'
alient_0["num"]=8
alient_0["list"]=herfood
print(alient_0)

for k,v in alient_0.items():
 print(k)
 print(v)

for m in  sorted(alient_0 ):
 print(m)


for m in alient_0.values():
     print(m)

city={
    'beijing':{'train':'k1','population':'1400M'},
    'Hangzhou':{'train':'T70','population':'700M'},
}
print(city)

for t,p in city.items():
    print(t)
    print("\t train is "+p['train'])
    print("\t populatin is "+p['population']+'\n')

prompt='打点字'
message=''
active=True
while active:
     message=input(prompt)
     if message=='q':
         active=False
     else:
         print(message)
     



