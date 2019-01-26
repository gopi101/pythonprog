a=int(input())
l=[]
while a>0:
   x=a%10
   a=a//10
   l.append(x)
for i in range(len(l)-1):
   print(l.pop(),end=" ")
print(l[0])
