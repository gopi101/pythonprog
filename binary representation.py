a=input()
temp=0
for c in a:
	if((c=='0')or(c=='1')):
		temp+=1
if(temp==(len(a))):
	print("yes")
else:
	print("no")	
