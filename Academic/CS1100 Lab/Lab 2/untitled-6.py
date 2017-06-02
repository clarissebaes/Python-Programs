def is_increasing(listicles):
    sort_list = listicles.sort()
    for n in listicles:
        i=0
        sort_list = listicles.sort()
        if n != sort_list[i]:
            return False
        
        
    
co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
                348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]        
    
print(is_increasing(co2_levels))
print('co2_levels is increasing: {}'.format(is_increasing(co2_levels)))
test_L1 = [ 15, 12, 19, 27, 45 ]
print('test_L1 is increasing: {}'.format(is_increasing(test_L1)))
test_L2 = [ 'arc', 'circle', 'diameter', 'radius', 'volume', 'area' ]
print('test_L2 is increasing: {}'.format(is_increasing(test_L2)))
test_L3 = [ 11, 21, 19, 27, 28, 23, 31, 45 ]
print('test_L3 is increasing: {}'.format(is_increasing(test_L3)))