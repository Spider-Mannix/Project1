#for averages use numpy/scipy
#https://stackoverflow.com/questions/7716331/calculating-arithmetic-mean-one-type-of-average-in-python
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
#check numpy stats library for useful information

import numpy
import column as cl 


slsmean = numpy.mean(cl.slset)
slsmed = numpy.median(cl.slset)
slsstd = numpy.std(cl.slset)

print(slsmean)
print(slsmed)
print(round(slsstd,2))