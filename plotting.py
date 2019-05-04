#from Problem 10 
import matplotlib.pyplot as pl
import numpy
import column as cl 
import minmax as mm

#plot sepal length for each class
a1 = cl.slset
a1 = [float(i) for i in a1]
a1.sort()
b1 = cl.slvers
b1 = [float(i) for i in b1]
b1.sort()
c1 = cl.slgin
c1 = [float(i) for i in c1]
c1.sort()
#converted to floats due to strings creating incorrect y-axis

#sepal width
a2 = cl.swset
a2 = [float(i) for i in a2]
a2.sort()
b2 = cl.swvers
b2 = [float(i) for i in b2]
b2.sort()
c2 = cl.swgin
c2 = [float(i) for i in c2]
c2.sort()

#petal length
a3 = cl.plset
a3 = [float(i) for i in a3]
a3.sort()
b3 = cl.plvers
b3 = [float(i) for i in b3]
b3.sort()
c3 = cl.plgin
c3 = [float(i) for i in c3]
c3.sort()

#petal width
a4 = cl.pwset
a4 = [float(i) for i in a4]
a4.sort()
b4 = cl.pwvers
b4 = [float(i) for i in b4]
b4.sort()
c4 = cl.pwgin
c4 = [float(i) for i in c4]
c4.sort()

pl.plot(a1)
pl.plot(b1)
pl.plot(c1)
pl.show()

pl.plot(a2)
pl.plot(b2)
pl.plot(c2)
pl.show()

pl.plot(a3)
pl.plot(b3)
pl.plot(c3)
pl.show()

pl.plot(a3)
pl.plot(b3)
pl.plot(c3)
pl.show()

#pl.scatter(mm.maxes, mm.mins)
#pl.show()
#from problem 10 
#seplen.sort()
#pl.plot(seplen)
#sepwit.sort()
#pl.plot(sepwit)
#slhist = numpy.histogram(seplen)
#pl.plot(slhist)
#l.show()