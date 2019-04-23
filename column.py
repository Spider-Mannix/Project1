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
    sepwit.append(x.split(',')[1])
    petlen.append(x.split(',')[2])
    petwit.append(x.split(',')[3])
    cliris.append(x.split(',')[4])

#close file (good practice)  
f.close()

print(cliris)  
print(len(cliris))

#code can now be used in other python files