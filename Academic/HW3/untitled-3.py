co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

avg = sum(co2_levels)/len(co2_levels)
above_avg = []
for levels in co2_levels:
    if levels > avg:
        above_avg.append(levels)
        
print('Average: {:.2f}'.format(avg))
print('Num above average: {:}'.format(len(above_avg)))

