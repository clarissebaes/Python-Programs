import hw4_util


def move(x,y,direction): #this move function is based of the turtle function. depending on what direction the player inputs determines is you +/- to the x/y
    if direction == 'e':
        x+=1
        x = min(x,10) #This min and max ensures that the player doesnt go past the 11X11 board
        x = max(x,0)
        return[x,y]
    elif direction == 'w':
        x-=1
        x = min(x,10)
        x = max(x,0)
        return[x,y]
    elif direction == 'n':
        y-=1
        y = min(y,10)
        y = max(y,0)
        return[x,y]
    elif direction == 's':
        y+=1
        y = min(y,20)
        y = max(y,0)
        return[x,y]


def capture(x,y): #this compares the player coordinates with the pokemons coordinates. if the coordinate are the same then the pokemon is captured and remonved from the list
    coord = (x,y)
    if coord in locations:
        n = locations.index(coord)
        pman = pokemon[n]
        print('You capture a {:} on turn {:}'.format(pman, t-1))
        locations.pop(n)
        pokemon.pop(n)

def print_pokemon(pokemon): #this prints the currently avaiable pokemon, if the pokemon is captured it is no longer on this list 
    print('Current pokemon:')
    for i in range(len(pokemon)):
        print('    ',pokemon[i] , 'at', locations[i])
    print()    
    

#main code starts here
pokemon, locations = hw4_util.read_pokemon()
 
x = 5
y= 5

print_pokemon(pokemon)

t = 0 #t counts the turns, each input incriments t and keeps track of the number turns


while t >= 0: #loop runs while t is positive, so to end the loop t=-1 and you exit the loop
    capture(x,y) #checks each coordinate if you capture a pokemon
    user_input = input( "N,S,E,W to move, 'print' to list, or 'end' to stop ==> ")
    print(user_input)
    command = user_input.lower() #makes sure that answer isnt case sensitive
    capture(x,y)
    if command == 'n':
        (x,y) = move(x,y,'n')
        print('Currently at ({:}, {:})'.format(x,y))
        t+=1
    elif command == 's':
        (x,y,) = move(x,y,'s')
        print('Currently at ({:}, {:}) '.format(x,y))
        t+=1
    elif command == 'e':
        (x,y) = move(x,y,'e')
        print('Currently at ({:}, {:})'.format(x,y))
        t+=1
    elif command == 'w':
        (x,y,) = move(x,y,'w')
        print('Currently at ({:}, {:})'.format(x,y))
        t+=1
    elif command == 'print':
        print('Current pokemon:')
        t+=1
        for i in range(len(pokemon)):
            print('    ',pokemon[i] , 'at', locations[i])
        print()
        print('Currently at ({:}, {:})'.format(x,y))
    elif command == 'end':
        t = -1
    else:
        print('Currently at ({:}, {:})'.format(x,y))
        

        
    
                   
            