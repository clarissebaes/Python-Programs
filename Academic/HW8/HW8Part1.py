from Pig import *
from Bird import *
from Barrier import *

def makelist(textz):
    thing_list = textz.strip().split('\n')
    i=0
    for thing in thing_list:
        thing = thing.split('|')
        thing_list[i] = thing
        i+=1
    return thing_list
def intersect( center1, center2, radius1, radius2):
    centDistance = ((((center1[0] -center2[0])**2) + (center1[1] -center2[1])**2)**.5)
    radiDistance = (radius1 + radius2)
    if centDistance <= radiDistance:
        return True
    else:
        return False

if __name__ == "__main__":
    bird_file = input('Enter bird file ==> ')
    print(bird_file)
    pig_file = input('Enter pig file ==> ')
    barrier_file = input('Enter barrier file ==> ')
    birdz = open(bird_file).read()
    pigz = open(pig_file).read()
    barrierz = open(barrier_file).read()
    birdlisticle = (makelist(birdz))
    birdlist = []
    for bird in birdlisticle:
        x = Bird(bird[0],bird[1],bird[2],bird[3],bird[4],bird[5],bird[6])
        birdlist.append(x)
    print('There are {} birds:'.format(len(birdlist)))
    for bird in birdlist:
        name = Bird.name(bird)
        position = Bird.position(bird)
        print('\t{}: {}'.format(name,position))
    piglisticle = (makelist(pigz))
    piglist = []
    for pig in piglisticle:
        x = Pig(pig[0],pig[1],pig[2],pig[3])
        piglist.append(x)
    print('There are {} pig:'.format(len(piglist)))
    for pig in piglist:
        name = Pig.name(pig)
        position = Pig.position(pig)
        print('\t{}: {}'.format(name,position))    
    barrierlisticle = (makelist(barrierz))
    barrierlist = []
    for barrier in barrierlisticle:
        x = Barrier(barrier[0],barrier[1],barrier[2],barrier[3],barrier[4])
        barrierlist.append(x)
    print('There are {} barriers:'.format(len(barrierlist)))    
    for barrier in barrierlist:
        name = Barrier.name(barrier)
        position = Barrier.position(barrier)
        print('\t{}: {}'.format(name,position))
        
        
    t = 1
    while t<100:
        if len(birdlist) >0:
            Bird.fly(birdlist[0])
            x,y = Bird.position(birdlist[0])
            radius1 = Bird.radius(birdlist[0])
            pos = (x,y)
            Bdname = Bird.name(birdlist[0])
            print('Time {}: {} at {}'.format(t, Bdname, pos))
            
            for pig in piglist:
                center1 = pos
                center2 = Pig.position(pig)
                radius2 = Pig.radius(pig)
                Pname = Pig.name(pig)
                o = intersect(center1,center2, radius1,radius2)
                print(o)
                if o == True:
                    piglist.remove(pig)
                    print('Time {}: {} at {} pops {}'.format(t,Bdname,pos, Pname))
                    Bird.lowerspeedpig(birdlist[0])
                    speed = (Bird.speed(birdlist[0]))
                    print('Time {}: {} at {} has (dx, dy) = {}'.format(t,Bdname,pos,speed))
                
                    
            t+=1
            


