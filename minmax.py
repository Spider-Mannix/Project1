#use sort()?
import column as cl

slmin = float(min(cl.seplen))
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

#using floats gives rounding error, must address - used round()
print(round(sldelta,1))