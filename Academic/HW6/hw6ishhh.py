def print10(lists):
    for i in range(10):
        print('{}. {}'.format(i+1,lists[i][1]))
def viloverlap(targetvil,vil_lists):
    targetset = targetvil[2]
    overlapset = []
    for vil in vil_lists:
        if targetvil[1]!= vil[1]:
            vilset = vil[2]
            if len(vilset & targetset)>0: 
                overlapset.append(vil)
    return overlapset
def makelist(lists):
    for i in range(len(lists)):
        print('{}. {}'.format(i+1,lists[i][1]))

vil_file = open('DrWhoVillains.tsv')
rankedvils=[]  
    

for line in vil_file:
    line = line.strip()
    vilinfo = line.split('\t')
    name = vilinfo[0].strip()
    shows = vilinfo[7] 
    shows = shows.strip().strip('\n')
    showlist = shows.split(',')
    for i in range(len(showlist)):
        showlist[i] = showlist[i].strip().lower()
    showset = set(showlist)
    shownum = len(showset)
    output = [shownum, name, showset]
    rankedvils.append(output)
rankedvils.sort()
rankedvils = rankedvils[::-1]
rankedvilsog = rankedvils.copy()

intarget_vil = (input('Who are you trying to reach? '))
target_vil = intarget_vil.lower()
print(intarget_vil)
print()
print10(rankedvils)

while True:
    rank = input('Enter a selection => ')
    print(rank)
    if rank.isdigit() == True:
        if int(rank) <= 10 and int(rank)>0:
            break
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

while target_vil != nextvil.lower():
    if rankedvils[rank-1][0] == 1:
        print('{} appeared in {} story and overlapped with:'.format(nextvil,rankedvils[rank-1][0]))
        
    else:
        print('{} appeared in {} stories and overlapped with:'.format(nextvil,rankedvils[rank-1][0]))
    print()
    targetvil = rankedvils[rank-1]
    listz = viloverlap(targetvil,rankedvilsog)
    makelist(listz) 
    rankedvils = listz
    while True:
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
    nextvil = rankedvils[rank-1][1]
    targetvil = rankedvils[rank-1]
print('You reached the villain {} in {} steps.'.format(nextvil,
 count))
print('Have a nice day.')
  