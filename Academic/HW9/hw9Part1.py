'''
This program finds the categories that overlap with a user inputed category
'''
import json
f = open('businesses.json')
category = input('Enter a category ==> ')
print(category)
cutoff = int(input('Cutoff for displaying categories => '))
print(cutoff)
overlap = dict() #reates a dictionary for the overlapping categories
for line in f:
    business = json.loads(line)
    catlist = business['categories'] #creates a list of the businesses categories
    if category in catlist: #makes usre the category is not the user inputed category
        for othercatz in catlist:
            if category != othercatz:       
                if othercatz not in overlap:
                    overlap[othercatz] = 0 #if the category is not in the dictionary it creates it as a key and keeps track of how many times it co-occurs
                if othercatz in overlap:
                    overlap[othercatz] +=1 #incraments the value each time it appears with the user inputted category 
count = 0
if len(overlap) == 0:
    print('Searched category is not found')
    count +=1
else:
    print('Categories co-occurring with {}:'.format(category))
    for category in sorted(overlap.keys()):
        if overlap[category]>= cutoff: #uses cut off to print only the categories above the cut off
            print(('{}: {}'.format(category,overlap[category])).rjust(33))
            count+=1
if count == 0:
    print('None above the cutoff')
            
    
    

