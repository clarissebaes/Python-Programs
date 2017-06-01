import hw4_util
'Cattaraugus'
area1 = input('Enter the first area to check => ')
print(area1)
cdata1 = hw4_util.read_deaths(area1)

if cdata1 == []:
    print(area1,'is an invalid name')
    sys.exit()

area2 = input('Enter the second area to check => ')
print(area2) 
cdata2 = hw4_util.read_deaths(area2)

if cdata2 == []:
    print(area2,'is an invalid name')
    sys.exit()

trend = []

for i in range(10,-1,-1):
    if cdata2[i] - cdata1[i] == 0 or abs(cdata2[i] - cdata1[i]) <= 50: 
        trend.append('=')
    elif cdata2[i] - cdata1[i] < -50:
        trend.append('-')
    elif cdata2[i] - cdata1[i] > 50:
        trend.append('+')


trend_out = (trend[0] + trend[1] + trend[2] + trend[3] + trend[4] + trend[5] + trend[6] + trend[7] + trend[8] + trend[9] + trend[10])

print('       ', '2103','   ','2003', sep = '')
print('Trend: ' + trend_out)

pluscount = trend_out.count('+')
minuscount = trend_out.count('-')


if pluscount > minuscount:
    print('I would rather live in {} than {}'.format(area1,area2))
elif pluscount < minuscount:
    print('I would rather live in {} than {}'.format(area2,area1))    
    
    

