#use sort()?
import column as cl

#sepal length
slsmin = float(min(cl.slset))
slsmax = float(max(cl.slset))
slsdelta = slsmax - slsmin

slvmin = float(min(cl.slvers))
slvmax = float(max(cl.slvers))
slvdelta = slvmax - slvmin

slgmin = float(min(cl.slgin))
slgmax = float(max(cl.slgin))
slgdelta = slgmax - slgmin

#sepal width
swsmin = float(min(cl.swset))
swsmax = float(max(cl.swset))
swsdelta = swsmax - swsmin

swvmin = float(min(cl.swvers))
swvmax = float(max(cl.swvers))
swvdelta = swvmax - swvmin

swgmin = float(min(cl.swgin))
swgmax = float(max(cl.swgin))
swgdelta = swgmax - swgmin

#petal length
plsmin = float(min(cl.plset))
plsmax = float(max(cl.plset))
plsdelta = plsmax - plsmin

plvmin = float(min(cl.plvers))
plvmax = float(max(cl.plvers))
plvdelta = plvmax - plvmin

plgmin = float(min(cl.plgin))
plgmax = float(max(cl.plgin))
plgdelta = plgmax - plgmin

#petal width
pwsmin = float(min(cl.pwset))
pwsmax = float(max(cl.pwset))
pwsdelta = pwsmax - pwsmin

pwvmin = float(min(cl.pwvers))
pwvmax = float(max(cl.pwvers))
pwvdelta = pwvmax - pwvmin

pwgmin = float(min(cl.pwgin))
pwgmax = float(max(cl.pwgin))
pwgdelta = pwgmax - pwgmin









#get min and max
#print(seplen)  
print(plgmin)
print(slgmax)

#using floats gives rounding error, must address - used round()
print(round(slgdelta,1))