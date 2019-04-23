#use sort()?
f=open("irisdata.txt","r")
lines=f.readlines()

seplen=[]
sepwit=[]
petlen=[]
petwit=[]
cliris=[]

for x in lines:
    seplen.append(x.split(',')[0])
    sepwit.append(x.split(',')[1])
    petlen.append(x.split(',')[2])
    petwit.append(x.split(',')[3])
    cliris.append(x.split(',')[4].rstrip('\n')) 

f.close()

seplen.sort()

print(seplen)  
print(len(seplen))
print(seplen[0])
print(seplen[len(seplen)-1])