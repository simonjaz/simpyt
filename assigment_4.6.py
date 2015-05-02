#Vnesi stevilo ur, dan v tednu izracunaj sestevek ur v tednu

def computepay(h,r):
    print "IN computepay h=", h, "r=", r
    if h <= 40 :
       p = h * r
    if h > 40 :
       p = r * 40 + (r * 1.5* (h -40))
    print "Finished with computepay", p
    return p

try:
    inp = raw_input("Enter Hours: ")
    hours = float(inp)
    inp = raw_input("Enter Rate: ")
    rate = float(inp)
except:
    print "Error, please enter numeric input"
    quit()

print "in the main code", rate, hours
pay = computepay (hours, rate)
print "We are back", pay
z = computepay(12.2, 10.0)
print "ZZZZZ", z
