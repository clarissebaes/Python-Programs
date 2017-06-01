'''
This program ask the user for a business input and prints out the reviews
if mor ethan one location exist, it ask which location the user wants to use
'''
import json
import textwrap
wrapper = textwrap.TextWrapper( initial_indent = ' '*4, subsequent_indent = ' '*4 )
def getrevs(file): #fucntion to get the reviews form the json file/ dictionary and prints it in the proper format
    revf = open(file)
    count = 1
    rev_avaiable = 'no'
    for line in revf:
        reviews = json.loads(line)
        bizid = reviews['business_id']
        if bizid == revdict['business_id']:
            print()
            print('Review: {}'.format(count))
            rev = str(reviews['text'].strip())
            rev = rev.split('\n\n')
            for line in rev:
                line = line.strip()
                linef = wrapper.wrap(line) #formats the review using text wrapper
                for line in linef:
                    print('{}'.format(line))
                print()
            count+=1
            rev_avaiable = 'yes'
    if rev_avaiable == 'no': #if no review exist prints out statement below
        print('No reviews for this business are found')
if __name__ == '__main__':
    revf = open('reviews.json')
    bizf = open('businesses.json')
    bizname = input('Enter a business name => ')
    print(bizname)
    
    revdict = dict()
    bizidlist = []
    for line in bizf: #creats a list of business ids 
        business = json.loads(line)
        name = business['name']
        if bizname == name:
            bizidlist.append(business['business_id'])
    bizf = open('businesses.json')       
    if len(bizidlist) == 1:
        for line in bizf:
            business = json.loads(line)
            name = business['name']
            if bizname == name: #checks if the inputed name and business name match
                revdict['full_address'] = business['full_address']
                revdict['business_id'] = business['business_id']
        print()
        print('Using {} at:'.format(bizname))
        print(revdict['full_address'])
        getrevs('reviews.json') #prints the review
    if len(bizidlist) > 1: #if the business has more htan one location
        print()
        print("Found {} at:".format(bizname))
        print()
        locdict = dict()
        loclist = [] #list of all the location 
        revloclist = [] #list of associated reviews
        for line in bizf:
                    business = json.loads(line)
                    name = business['name']
                    if bizname == name:
                        loclist.append(str(business['full_address']))
                        revloclist.append(business['business_id']) #adds ID to business id list
                        location = str(business['full_address'])
                        locdict[location] = business['business_id']
        count = 1
        for location in loclist:
            print('{}.'.format(count))
            print(location)
            print()
            count +=1
        choice = -1
        while choice<1 or choice> len(locdict): #while loop to make sure user inputs a vaild choice 
            choice = int(input('Select one from 1 - {} ==> '.format(len(locdict))))
            print(choice)
        print()
        print('Using Hannaford Supermarkets at:')
        print('{}'.format(loclist[choice-1]))
        revdict['full_address'] = loclist[choice-1]
        revdict['business_id'] = revloclist[choice-1]
        getrevs('reviews.json')        
        
        
    if len(bizidlist) == 0: #if the business isnt found 
        print('This business is not found')

         
                        













  
        