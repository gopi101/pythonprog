x,a,b=map(int,input().split(" "))
sum=0
for i in range(x):
    x=a+i*b
    sum=sum+x
print(sum)
