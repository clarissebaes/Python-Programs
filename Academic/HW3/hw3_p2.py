import hw3_util

def 

legos = hw3_util.read_legos('legos.txt')
print(legos)

leggo_need = input('What type of lego do you need ==> ')
print(leggo_need)

onebyone = legos.count('1x1')
twobyone = legos.count('2x1')
twobytwo = legos.count('2x2')
twobyfour = legos.count('2x4')

if leggo_need == '1x1':
    total = onebyone
    print('I can make {:} 1X1 pieces:'.format(total))
    print('  ','0 pieces of 1X1 using 2x4 pieces',sep = '')
    print('  ','0 pieces of 1X1 using 2x2 pieces',sep = '')
    print('  ','0 pieces of 1X1 using 2x1 pieces',sep = '')
    print('  ','{:} pieces of 1X1 using 1x1 pieces'.format(total),sep='')

    