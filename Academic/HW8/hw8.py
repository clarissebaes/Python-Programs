from Pig import *
from Bird import *
from Barrier import *

def makelist(textz): #this takes the info from the file outputs it in a list of list
    #you need this so you can pass the info as an atributes of the respective object
    thing_list = textz.strip().split('\n')
    i=0
    for thing in thing_list:
        thing = thing.split('|')
        thing_list[i] = thing
        i+=1
    return thing_list
def intersect( center1, center2, radius1, radius2): #test the intersection of the
    #rdius. Can be used for barrier and pig intersection
    centDistance = ((((center1[0] -center2[0])**2) + (center1[1] -center2[1])**2)**.5)
    radiDistance = (radius1 + radius2)
    #checks if the distance between the center is less than the sum of the radi
    if centDistance <= radiDistance:
        return True #intersected
    else:
        return False #didnt intersect
if __name__ == "__main__":
    bird_file = input('Enter the name of the bird file => ')
    print(bird_file)
    pig_file = input('Enter the name of the pig file => ')
    print(pig_file)
    barrier_file = input('Enter the name of the barrier file => ')
    print(barrier_file)
    print()
    birdz = open(bird_file).read()
    pigz = open(pig_file).read()
    barrierz = open(barrier_file).read()
    birdlisticle = (makelist(birdz))
    birdlist = []
    for bird in birdlisticle:
        x = Bird(bird[0],bird[1],bird[2],bird[3],bird[4],bird[5],bird[6])
        #passes the info as atributes of  Bird class
        birdlist.append(x)
        #birdlist is a list of objects
    #below prints all the info all nice
    print('There are {} birds:'.format(len(birdlist)))
    for bird in birdlist:
        Bdname = Bird.name(bird)
        Bdposition = Bird.position(bird)
        Bdxpos = Bird.xpos(bird)
        Bdypos = Bird.ypos(bird)        
        print('    {}: ({},{})'.format(Bdname,Bdxpos,Bdypos))
    piglisticle = (makelist(pigz))
    piglist = []
    for pig in piglisticle:
        x = Pig(pig[0],pig[1],pig[2],pig[3])
        piglist.append(x)
    print()
    print('There are {} pigs:'.format(len(piglist)))
    for pig in piglist:
        Pname = Pig.name(pig)
        position = Pig.position(pig)
        Pxpos = Pig.xpos(pig)
        Pypos = Pig.ypos(pig)                
        print('    {}: ({},{})'.format(Pname,Pxpos,Pypos))    
    barrierlisticle = (makelist(barrierz))
    barrierlist = []
    for barrier in barrierlisticle:
        x = Barrier(barrier[0],barrier[1],barrier[2],barrier[3],barrier[4])
        barrierlist.append(x)
    print()
    print('There are {} barriers:'.format(len(barrierlist)))    
    for barrier in barrierlist:
        Barname = Barrier.name(barrier)
        position = Barrier.position(barrier)
        Barxpos = Barrier.xpos(barrier)
        Barypos = Barrier.ypos(barrier)        
        print('    {}: ({},{})'.format(Barname,Barxpos, Barypos))
    #printing stuff ends
    #I have birdlist[0] since I alsways use the first bird object in the list
    #even if I pop the bird out, the rest of the birds move down an index
    #so you always refrence birdlist[0]
    xpos = Bird.xpos(birdlist[0])
    ypos = Bird.ypos(birdlist[0])    
    print(Bird.name(birdlist[0]))  
    print()   
    t = 0
    print('Time 0: {} starts at ({},{})'.format(Bird.name(birdlist[0]),xpos, ypos))
    while t<1000: #stops me from having an infinite loop just incase I mess up
        t+=1 #incrementing for time
        if len(birdlist) >0: #makes sure all the birds didnt die
            #set bird variables
            Bird.fly(birdlist[0])
            x,y = Bird.position(birdlist[0])
            radius1 = Bird.radius(birdlist[0])
            pos = (x,y)
            xpos = Bird.xpos(birdlist[0])
            ypos = Bird.ypos(birdlist[0])
            dx = Bird.dxpos(birdlist[0])
            dy = Bird.dypos(birdlist[0])            
            Bdname = Bird.name(birdlist[0])
            
            for pig in piglist: #runs through all alive pigs to check intersection
                center1 = pos
                center2 = Pig.position(pig)
                radius2 = Pig.radius(pig)
                Pname = Pig.name(pig)
                o = intersect(center1,center2, radius1,radius2)
                # if o is True Intersection happened
                if o == True: 
                    piglist.remove(pig) #if intersection happens pig dies and is popped
                    print('Time {}: {} at ({},{}) pops {}'.format(t,Bdname,xpos, ypos, Pname))
                    Bird.lowerspeedpig(birdlist[0]) #reduce the speed of the bird
                    speed = (Bird.speed(birdlist[0]))
                    #have to redefine new coordinates
                    dx = Bird.dxpos(birdlist[0]) 
                    dy = Bird.dypos(birdlist[0])                                
                    print('Time {}: {} at ({},{}) has (dx, dy) = ({},{})'.format(t,Bdname,xpos, ypos, dx, dy))
            
            for barrier in barrierlist: #run through barriers to check intersection
                center1 = pos
                center2 = Barrier.position(barrier)
                radius2 = Barrier.radius(barrier)
                Barname = Barrier.name(barrier)
                o = intersect(center1,center2, radius1,radius2)#same idea as pigs
                if o == True:
                    strength = Barrier.strength(barrier) #barrier strenght is decreased if intersection happened
                    damage = Bird.damagegiven(birdlist[0])
                    finstrength = strength - damage
                    if finstrength < 0: #if strenght is negative its just 0
                        finstrength = 0.0
                    print('Time {}: {} at ({},{}) hits {}, Strength {}'.format(t, Bdname, xpos, ypos, Barname, finstrength))
                    if finstrength == 0: #if stength is 0 barrier crumbles and is popped
                        print('Time {}: {} crumbles'.format(t,Barname))
                        print('Time {}: {} at ({},{}) has (dx, dy) = (0.0,0.0)'.format(t,Bdname,xpos, ypos))
                    #Bird.lowerspeedpig(birdlist[0]) #lower the speed of the bird
                    speed = (Bird.speed(birdlist[0]))
                    print('Time {}: {} at ({},{}) with speed 0.0 stops'.format(t,Bdname,xpos,ypos ))
                    birdlist.pop(0)#bird dies wen intersection with barrier happens and is popped
                    xpos = Bird.xpos(birdlist[0]) #new bird so redefine coordinates
                    ypos = Bird.ypos(birdlist[0])                    
                    print('Time {}: {} starts at ({},{})'.format(t,Bird.name(birdlist[0]),xpos, ypos))
            birdvel = Bird.birdvelocity(birdlist[0]) #checks the bird velocity
            if birdvel <6: #if bird velocity is less than 6 bird dies and is popped
                print('Time {}: {} at ({},{}) with speed {} stops'.format(t, Bdname, xpos, ypos, birdvel))
                birdlist.pop(0)
                if len(birdlist) != 0: #makes sure you still have birds available
                    xpos = Bird.xpos(birdlist[0])
                    ypos = Bird.ypos(birdlist[0])                
                    print('Time {}: {} starts at ({},{})'.format(t,Bird.name(birdlist[0]),xpos, ypos))
                if len(piglist) == 0: # checks if you stil have pigs available
                    print('Time {}: All pigs are popped. The birds win!'.format(t))
                    break  
            bordertest = Bird.inboard(birdlist[0]) #checks if bird is still within the boarder
            if bordertest == True: #if true bird flew off boarder and bird dies
                print('Time {}: {} at ({},{}) has left the game'.format(t, Bdname, xpos, ypos))
                birdlist.pop(0)
                
                if len(birdlist) != 0:
                    xpos = Bird.xpos(birdlist[0])
                    ypos = Bird.ypos(birdlist[0])                    
                    print('Time {}: {} starts at ({},{})'.format(t,Bird.name(birdlist[0]),xpos, ypos))
                else:
                    print('Time {}: No more birds. The pigs win!'.format(t))
                    print('Remaining pigs:')
                    piglisticle = piglist.copy()
                    for pig in piglisticle:
                        Pname = Pig.name(pig)
                        print('{}'.format(Pname))
            if len(piglist) == 0:
                print('Time {}: All pigs are popped. The birds win!'.format(t))
                break
            
        

                
                
                
                
                    
        
            


