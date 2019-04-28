#for averages use numpy/scipy
#https://stackoverflow.com/questions/7716331/calculating-arithmetic-mean-one-type-of-average-in-python
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
#check numpy stats library for useful information

import numpy

f=open("irisdata.txt","r")
lines=f.readlines()

seplen=[]
sepwit=[]
petlen=[]
petwit=[]
cliris=[]

for x in lines:
    seplen.append(x.split(',')[0])
    seplen = [float(i) for i in seplen]
    sepwit.append(x.split(',')[1])
    petlen.append(x.split(',')[2])
    petwit.append(x.split(',')[3])
    cliris.append(x.split(',')[4].rstrip('\n')) 

f.close()
#sltot = sum(seplen)
#slmean = sltot / len(seplen)
#print(round(slmean,1))
slmean = numpy.mean(seplen)

print(slmean)