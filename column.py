f=open("irisdata.txt","r")
lines=f.readlines()
result=[]
for x in lines:
    result.append(x.split(',')[0])
  
f.close()

print(result)  