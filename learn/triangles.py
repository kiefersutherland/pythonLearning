def triangles():
     L=[1] 
     while True: yield L 
     L=[L[i]+L[i+1] for i in range(len(L)-1)] 
     L.insert(0,1) 
     L.append(1)


t=triangles()
print(t)

for c in t:
    print(c)