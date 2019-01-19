a=5
b=[]
b.append(1)
b.append(1)
for x in range(2,a):
    b.append(b[x-1]+b[x-2])
for x in range(0,len(b)):
    print(b[x]," ")
