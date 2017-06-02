import lab05_util
restaurants = lab05_util.read_yelp('yelp.txt')

def print_info(num):
    num = int(num)
    address = restaurants[num][3].split("+")
    avg_score = sum(restaurants[num][6])/len(restaurants[0][6])
    print(restaurants[num][0], '({:})'.format(restaurants[num][5]))
    print('\t',address[0],sep = '')
    print('\t',address[1],sep = '')
    print('\t','Average Score: {:.2f}'.format(avg_score),sep = '')
    print()
    
print_info(0)
print_info(1)
print_info(2)
print_info(3)
print_info(4)