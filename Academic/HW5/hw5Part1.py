import random
import time

def capture_pokemon(prob):
    captureprob = random.random()
    if captureprob < prob:
        return 1
    else:
        return 0
def move_trainer(position,bounds, prob):
    direction = random.randint(0,3)
    row=position[0]
    col=position[1]
    capture = capture_pokemon(prob)
    if direction == 0:
        row-=1
        row = min(row,bounds[0])
        row = max(row,0)
        position = (row,col)
        output = (position,capture)
        return output
    elif direction == 1:
        row+=1
        row = min(row,bounds[0])
        row = max(row,0)
        position = (row,col)
        output = (position,capture)
        return output
    elif direction == 2:
        col+=1
        col = min(col,bounds[1])
        col = max(col,0)
        position = (row,col)
        output = (position,capture)
        return output
    elif direction == 3:
        col-=1
        col = min(col,bounds[1])
        col = max(col,0)
        position = (row,col)
        output = (position,capture)
        return output



mrow = int(input('Enter the integer number of rows => '))
print(mrow)
ncol = int(input('Enter the integer number of cols => '))
print(ncol)
prob = float(input('Enter the probability of finding a pokemon (<= 1.0) => '))
print(prob)

seed_value = 10*mrow + ncol
random.seed(seed_value)

bounds = (mrow-1,ncol -1)

row = mrow//2
col = ncol//2

position = (row,col)

pokenumturn = 0
pokenumtotal = 0
i=0

while i < 250:
    output = (move_trainer(position,bounds,prob))
    position= output[0]
    pokenumtotal += output[1]
    pokenumturn += output[1]
    i+=1
    if i%20 == 0:
        turn = i
        print('Time step {:}: position {:} pokemon caught since the last report {:}'.format(turn, position, pokenumturn))
        pokenumturn = 0

print('After 250 time steps the trainer ended at position {:} with {:} pokemon.'.format(position,pokenumtotal))
    

