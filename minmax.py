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

slmin = float(min(seplen))
slmax = float(max(seplen))
sldelta = slmax - slmin

swmin = float(min(sepwit))
swmax = float(max(sepwit))
swdelta = swmax - swmin

plmin = float(min(petlen))
plmax = float(max(petlen))
pldelta = plmax - plmin

pwmin = float(min(petwit))
pwmax = float(max(petwit))
pwdelta = pwmax - pwmin

#get min and max
#print(seplen)  
print(slmin)
print(slmax)

#using floats gives rounding error, must address
print(sldelta)