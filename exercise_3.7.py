#inp = raw_input('Enter Fahrenheit Temperature:') 
#fahr = float(inp)
#cel = (fahr - 32.0) * 5.0 / 9.0
#print cel
np = raw_input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0 
    print cel
except:
    print 'Please enter a number'