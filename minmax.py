#use sort()?
f=open("irisdata.txt","r")
lines=f.readlines()
result=[]
for x in lines:
   seplen = result.append(x.split(',')[0])
  
f.close()

result.sort()
print(result)  
print(len(result))