import hw3_util
'''
leggo_Stats takes the info from the if statements that determine the leggo conversion and prints it in the output format
'''

def leggo_stats(total, leggo_want, use_2x4, use_2x2, use_2x1, use_1x1):    
    print('I can make {:} {:} pieces:'.format(total,leggo_want))
    print('     ','{:} pieces of {:} using 2x4 pieces.'.format(use_2x4, leggo_want),sep = '')
    print('     ','{:} pieces of {:} using 2x2 pieces.'.format(use_2x2, leggo_want),sep = '')
    print('     ','{:} pieces of {:} using 2x1 pieces.'.format(use_2x1, leggo_want),sep = '')
    print('     ','{:} pieces of {:} using 1x1 pieces.'.format(use_1x1,leggo_want),sep='')
    

legos = hw3_util.read_legos('legos.txt')

leggo_need = input('What type of lego do you need? ==> ')
print(leggo_need)
print()
'''
the count function counts how many of leggos in the list
'''
onebyone = int(legos.count('1x1'))
twobyone = int(legos.count('2x1'))
twobytwo = int(legos.count('2x2'))
twobyfour = int(legos.count('2x4'))

'''
depending on what the user inputs they get different conversions between the pieces
 the // ensures that only full leggos are out putted
if they input non of the recognized leggos it results in an error message
'''

if leggo_need == '1x1':
    total = onebyone
    leggo_stats(total,leggo_need, 0, 0, 0, onebyone) 
elif leggo_need == '2x1':
    use_1x1 = onebyone//2
    total = use_1x1 + twobyone
    leggo_stats(total,leggo_need, 0, 0, twobyone, use_1x1)
elif leggo_need == '2x2':
    use_2x1 = twobyone // 2
    use_1x1 = onebyone // 4
    total = use_2x1 + use_1x1 + twobytwo
    leggo_stats(total,leggo_need, 0, twobytwo, use_2x1, use_1x1)
elif leggo_need == '2x4':
    use_2x2 = twobytwo // 2 
    use_2x1 = twobyone // 4
    use_1x1 = onebyone // 8
    total = use_2x2 + use_2x1 + use_1x1 + twobyfour
    leggo_stats(total,leggo_need, twobyfour, use_2x2, use_2x1, use_1x1)
else:
    print('Illegal lego')
    