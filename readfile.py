
txt = "irisdata.txt"
fls = open(txt,'r')
x23 = fls.read()
lines = x23.split('\n')

#every second line
vnm = lines[::]

for i in vnm:
    print(i)