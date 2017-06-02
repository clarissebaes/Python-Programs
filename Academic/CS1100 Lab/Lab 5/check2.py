import lab05_util
restaurants = lab05_util.read_yelp('yelp.txt')

def output_score(avg_score,num_review):
    if avg_score > 0 and avg_score <= 2:
        return('This restaurant is rated bad, based on {:} reviews.'.format(num_review))
    elif avg_score > 2 and avg_score <= 3:
        return('This restaurant is rated average, based on {:} reviews.'.format(num_review))
    elif avg_score > 3 and avg_score <= 4:
        return('This restaurant is rated above average, based on {:} reviews.'.format(num_review))
    elif avg_score > 4 and avg_score <= 5:
        return('This restaurant is rated very good, based on {:} reviews.'.format(num_review))
    

def average_score(indx):
    if len(restaurants[indx][6]) > 3:
        no_max_min = (sum(restaurants[indx][6]) - max(restaurants[indx][6]) - min(restaurants[indx][6]))
        num_review = int((len(restaurants[indx][6]))) -2
        avg_score = no_max_min/num_review
        final_avg_score = output_score(avg_score,num_review) 
        return final_avg_score
    else:
        avg_score = sum(restaurants[indx][6])/len(restaurants[indx][6])
        num_review = len(restaurants[indx][6])
        final_avg_score = output_score(avg_score,num_review) 
        return final_avg_score

def print_info(indx):
    num = int(indx)
    address = restaurants[indx][3].split("+")
    avg_score = average_score(indx)
    print(restaurants[indx][0], '({:})'.format(restaurants[indx][5]))
    print('\t',address[0],sep = '')
    print('\t',address[1],sep = '')
    print('\t',avg_score,sep = '')
    print()
    
res_num = int(input('Enter a Restaurant ID ==> '))
indx = res_num-1

if indx>= 0 and indx<155:
    print_info(indx)
else:
    print('No Restaurant has that ID')
