#from https://stackoverflow.com/questions/30216573/reading-specific-columns-from-a-text-file-in-python

#open and read data file
f=open("irisdata.txt","r")
lines=f.readlines()

#variables for each attribute column: sepal length & width, petal length & width, and iris class
seplen=[]
sepwit=[]
petlen=[]
petwit=[]
cliris=[]

for x in lines:
    #use append to fill in blank lists
    seplen.append(x.split(',')[0])
    #separate by class
    slset = seplen[0:50]
    slvers = seplen[50:100]
    slgin = seplen[100:150]
    sepwit.append(x.split(',')[1])
    petlen.append(x.split(',')[2])
    petwit.append(x.split(',')[3])
    cliris.append(x.split(',')[4].rstrip('\n')) 

#rstrip removes '\n' from print - https://stackoverflow.com/questions/11280282/to-read-line-from-file-without-getting-n-appended-at-the-end

#close file (good practice)  
f.close()

print(slset)  
print(len(slset))
print(slvers)  
print(len(slvers))
print(slgin)  
print(len(slgin))

#code can now be used in other python files