a=input("")
b=['@','!','#','$','%','^','&','*','.','?']
count=0
for i in a:
    if i in b:
        count+=1
print(count)        
