#from Problem 10 
import matplotlib.pyplot as pl

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

#from problem 10 
seplen.sort()
pl.plot(seplen)
pl.show()