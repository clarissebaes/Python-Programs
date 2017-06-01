import hw4_util

area1 = input('Enter the first area to check => ')
print(area1)
cdata1 = hw4_util.read_deaths(area1)

if cdata1 == []: #This checks if the area is a valid county, if it is not valid the data list is empty 
    print(area1,'is an invalid name')
    sys.exit([arg])

area2 = input('Enter the second area to check => ')
print(area2) 
cdata2 = hw4_util.read_deaths(area2)

if cdata2 == []: #same as area1/cdata1 check1 
    print(area2,'is an invalid name')
    sys.exit([arg])

trend = []

for i in range(10,-1,-1): #the range starts at 10 then goes to 0 so it does the years backwards from 2013 to 2003
    if cdata2[i] - cdata1[i] == 0 or abs(cdata2[i] - cdata1[i]) <= 50: 
        trend.append('=')
    elif cdata2[i] - cdata1[i] < -50:
        trend.append('-')
    elif cdata2[i] - cdata1[i] > 50:
        trend.append('+')


trend_out = (trend[0] + trend[1] + trend[2] + trend[3] + trend[4] + trend[5] + trend[6] + trend[7] + trend[8] + trend[9] + trend[10]) # this takes each index of the trend list and outputs it in a string with no

print()
print('       ', '2013','   ','2003', sep = '')
print('Trend: ' + trend_out)
print()
pluscount = trend_out.count('+') #this counts the number of +
minuscount = trend_out.count('-')# this countds the number of -

# compares the plus and minus counts if more plus the first area is favored and vice versa with the minuses and area 2
if pluscount > minuscount:
    print('I would rather live in {} than {}'.format(area1,area2))
elif pluscount < minuscount:
    print('I would rather live in {} than {}'.format(area2,area1)) 
else:
    print('{} and {} are the same'.format(area1,area2))
    
    

