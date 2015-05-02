#Vnesi stevilo ur, dan v tednu izracunaj sestevek ur v tednu

inp = raw_input("Enter Hours: ")
hours = float(inp)
inp = raw_input("Enter Rate: ")
rate = float(inp)
# print rate, hours
if hours <= 40 :
    pay = hours * rate
if hours > 40 :
    pay = rate * 40 + (rate * 1.5* (hours -40))
print "Pay: ", pay
    