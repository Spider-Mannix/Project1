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
    seplen = [float(i) for i in seplen] #make floating point numbers
    #separate by class
    slset = seplen[0:50]
    slvers = seplen[50:100]
    slgin = seplen[100:150]

    sepwit.append(x.split(',')[1])
    sepwit = [float(i) for i in sepwit]
    swset = sepwit[0:50]
    swvers = sepwit[50:100]
    swgin = sepwit[100:150]

    petlen.append(x.split(',')[2])
    petlen = [float(i) for i in petlen]
    plset = petlen[0:50]
    plvers = petlen[50:100]
    plgin = petlen[100:150]

    petwit.append(x.split(',')[3])
    petwit = [float(i) for i in petwit]
    pwset = petwit[0:50]
    pwvers = petwit[50:100]
    pwgin = petwit[100:150]


    cliris.append(x.split(',')[4].rstrip('\n')) 

#rstrip removes '\n' from print - https://stackoverflow.com/questions/11280282/to-read-line-from-file-without-getting-n-appended-at-the-end

#close file (good practice)  
f.close()

#code can now be used in other python files