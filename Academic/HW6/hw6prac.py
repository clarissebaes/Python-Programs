'''
Clarisse Baes 11/3/2016
This program ask the user for their "Target Villain" and then prints out a top ten Villains list based on the
amount of stories they appear in. 
Then a list of the ovelapping villains is printed.
the user then makes a selection for the next villain.
this continues until the user picks their target villain.
'''
def print10(lists): #This function prints the top 10 villians list
    for i in range(10):
        print('{}. {}'.format(i+1,lists[i][1]))
def viloverlap(targetvil,vil_lists): #determines the overlap between a target villain and the rest of the villains
    targetset = targetvil[2] #this accesses the set of shows
    overlapset = []
    for vil in vil_lists:
        if targetvil[1]!= vil[1]:#this prevents the target villain from appearing in the overlap list
            vilset = vil[2]
            if len(vilset & targetset)>0: #if they share a story in common then their intersection set is >0
                overlapset.append(vil) #appends all the overlapped villians into a list
    return overlapset
def makelist(lists): # this prints the list(besides the top 10 list)
    for i in range(len(lists)):
        print('{}. {}'.format(i+1,lists[i][1]))
#main code starts below
if __name__ == '__main__':
    vil_file = open('DrWhoVillains.tsv') #file of all the villains with all the info
    rankedvils=[]  
    
    for line in vil_file:
        line = line.strip()
        vilinfo = line.split('\t') #splits the information from the file
        name = vilinfo[0].strip() #name of villain
        shows = vilinfo[7] #string of all the stories the villain appears in
        shows = shows.strip().strip('\n') 
        showlist = shows.split(',')
        for i in range(len(showlist)):
            showlist[i] = showlist[i].strip().lower()#strips and lowers each individual story name
        showset = set(showlist)#makes it a set so there are no repeats
        shownum = len(showset) #number of the stories
        output = [shownum, name, showset]#number is first so I can sort by amount of stories
        rankedvils.append(output)
    rankedvils.sort()
    rankedvils = rankedvils[::-1] #reverses set, so the largest number of stories is first
    rankedvilsog = rankedvils.copy()

    intarget_vil = (input('Who are you trying to reach? '))
    target_vil = intarget_vil.lower()
    print(intarget_vil)
    print()
    print10(rankedvils) #prints top 10 list

    while True:
        rank = input('Enter a selection => ')
        print(rank)
        if rank.isdigit() == True: #this loop makes sure that when the user inputs invalid input that the code continues and ask the user for input until a valid input is
            if int(rank) <= 10 and int(rank)>0:
                break #valid input leaves the loop
            else:
                print()
                print10(rankedvils)
                continue
            
        else:
            print()
            print10(rankedvils)
            continue
    rank= int(rank)
    print()
    nextvilset = rankedvils[rank-1]
    nextvil = nextvilset[1]
    count = 1
    while target_vil != nextvil.lower(): #loops until user reaches the target villain
        if rankedvils[rank-1][0] == 1:
            print('{} appeared in {} story and overlapped with:'.format(nextvil,rankedvils[rank-1][0]))
            print()
        else:
            print('{} appeared in {} stories and overlapped with:'.format(nextvil,rankedvils[rank-1][0]))
            print()
        targetvil = rankedvils[rank-1]
        listz = viloverlap(targetvil,rankedvilsog) #creates a list of overlapping villains
        makelist(listz) #prints said list
        rankedvils = listz
        while True: #same idea as the loop above to make sure that the input is valid
            rank = input('Enter a selection => ')
            print(rank)
            if rank.isdigit() == True:
                if int(rank) <= len(listz) and int(rank)>0:
                    break
                else:
                    print()
                    makelist(listz)
                    continue            
            else:
                print()
                makelist(listz)
                continue
            
        rank = int(rank)
        print()
        count+=1
        nextvil = rankedvils[rank-1][1] # redefines the variable with the new villain so the while loop can continue
        targetvil = rankedvils[rank-1]
    #once the name of the target villain == next villain then the loop is exited
    print('You reached the villain {} in {} steps.'.format(nextvil,count))
    print('Have a nice day.')