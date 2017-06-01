'''
this program simulates trainers catching a pokemon.
the pokemon have a set location and health and the trainers "throw pokeballs"
at set locations, iwht its with in a certain idstance the pokemon recieves damages
once th pokemon health reaches 0 it is catpured
'''

class Pokemon(object): #pokemon clas to keep track of the pokemon info 
    def __init__(self,n,x,y,r,h):
        self.poke_name = n
        self.poke_x = int(x)
        self.poke_y = int(y)
        self.poke_radius = int(r)
        self.poke_health = int(h)
    def position(self):
            return (self.poke_x, self.poke_y)
    def radius(self):
        return (self.poke_radius)
    def name(self):
        return self.poke_name
    def health(self):
        return self.poke_health
    def dec_health(self,damage): #decrease health function redfines the health if the pokeball is thrown with in range
        self.poke_health -= damage 


def intersection(pokecenter,traincenter, pokeradius): #function to check the distance between the pokemon and the ball
    centDistance = ((((pokecenter[0] -traincenter[0])**2) + (pokecenter[1] -traincenter[1])**2)**.5)
    if centDistance < int(pokeradius): #if the ball is with in the pokemon radius htey lose 2 health points
        return 2
    if centDistance < (int(pokeradius)+5): #if they are with in the pokemon radius and the pokeball radius they lose 1
        return 1
    else: #if they completely miss damage is 1
        return 0  

if __name__ == "__main__":
    infile = input('File name => ')
    print(infile)
    file = open(infile).read()
    filelisticle = file.strip().split('\n')
    poke_num = int(filelisticle[0]) #finds number of pokemon
    filelisticle.pop(0)
    pokelisticle = []
    opokelist = []
    for i in range(poke_num): #divides the list of pokemon and list of trainer
        pokemanz = filelisticle.pop(0)
        pokelisticle.append(pokemanz)
    for poke in pokelisticle: #pass the Pokemon infro through the class to create pokemon objects
        poke = poke.strip().split('|')
        print('{}:'.format(poke[0]).rjust(13), end='')
        print(' ({},{},{}) Health: {}'.format(poke[1],poke[2],poke[3],poke[4]).rjust(12))
        poke_obj = Pokemon(poke[0],poke[1],poke[2],poke[3],poke[4])
        opokelist.append(poke_obj)
    print()
    catchdict = dict() #dictionary of the caught pokemon for each trainer
    
    if len(opokelist) > 0: #makes sure there are still avaiable pokemon
        for trainer in filelisticle: #runs through the lines of trainers
            trainerlist = trainer.strip().split('|')
            name = trainerlist[0]
            if name not in catchdict:
                catchdict[name] = [] #creates the key for the trainers
            traincenter = (int(trainerlist[1]),int(trainerlist[2]))
            for poke in opokelist: #runs through list of pokemon
                pokecenter = (Pokemon.position(poke))
                pokeradius = Pokemon.radius(poke)
                damage = intersection(pokecenter,traincenter, pokeradius) #passes the pokemon and trainer center through the intersection function
                if damage != 0: #if there is damage then the trainer hits the pokemon
                    print('{} throws a pokeball to position {} hits {}:'.format(name,traincenter,Pokemon.name(poke)))
                    Pokemon.dec_health(poke,damage) #decrease health
                    if Pokemon.health(poke) <= 0: #if helath is below 0 then pokemon is captured
                        print('{}'.format(Pokemon.name(poke)).rjust(12), end='')
                        print(': ({},{},{}) Health: {}'.format(Pokemon.position(poke)[0],Pokemon.position(poke)[1],Pokemon.radius(poke),max(Pokemon.health(poke),0)).rjust(12))
                        print('{} is caught!'.format(Pokemon.name(poke)))
                        catchdict[name].append(Pokemon.name(poke))
                        opokelist.remove(poke) #removes pokemon from list
                        break 
                    print('{}'.format(Pokemon.name(poke)).rjust(12), end='')
                    print(': ({},{},{}) Health: {}'.format(Pokemon.position(poke)[0],Pokemon.position(poke)[1],Pokemon.radius(poke),Pokemon.health(poke)).rjust(12)) #prints health              
                    break
            if damage == 0: #if damge is 0 then the trainer missed
                print('{} misses at {}'.format(name,traincenter))
    if len(opokelist) == 0: 
        print()
        print('All pokemon caught, results:')
        for name in sorted(catchdict.keys()):
            print('{} caught {} pokemon'.format(name, len(catchdict[name]))) #prints caught dictionary and which trainer catches which pokemonq
            for poke in catchdict[name]:
                print(poke.rjust(12))
    else:
        print() 
        print('Players run out of pokeballs, results:')
        print(catchdict)
        for name in sorted(catchdict.keys()):
                    print('{} caught {} pokemon'.format(name, len(catchdict[name])))
                    for poke in catchdict[name]:
                        print(poke.rjust(12))        
                
            
            
            

    
    
    
    
