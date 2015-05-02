#Vnesi stevilo ur, dan v tednu izracunaj sestevek ur v tednu

hrs = raw_input("Enter Hours: ")
try:
    ival = int(hrs)
except:
    ival =-1
if ival < 0:
    print "Not a number"
#h = float(hrs)
rate = raw_input("Enter Rate: ")
try:
    ival = int(rate)
except:
    ival =-1
if ival < 0:
    print "Not a number"
#r = float(rate)
# print rate, hours
if h <= 40 :
    pay = h * r
else :
    pay = r * 40 + (r * 1.5* (h -40))
print "Pay: ", pay
