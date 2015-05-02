#vaja Worked Exercise 5.1
count = 0
total = 0
while True:
    inp = raw_input('Enter a number: ')
    
    #DHandle the edge cases
    if inp =='done' : break
    if len(inp) < 1 : break #Check for empty line
    try :
       num = float(inp)
    except:
        print "Invalid input"
        continue
    count = count + 1
    total = total + num
    print num, total, count

print 'Everage = ', total / count