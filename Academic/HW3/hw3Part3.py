'''
use the move function for both move(amount =20) and jump (amount = 50)

this function takes the input x,y coordinate and adds the apporopriate amount depending if its a move or jump 
and it then redfeines x,y with the new coordinate

also whether it adds or subtracts values to either the x or y coordinate depends on the direction the turtle isfacing

also the max and min function ensure that the turtle remains in the fence
'''
def move(x,y,direction,amount):
    if direction == 'right':
        x+=amount
        x = min(x,400)
        x = max(x,0)
        return[x,y,direction]
    elif direction == 'left':
        x-=amount
        x = min(x,400)
        x = max(x,0)
        return[x,y,direction]
    elif direction == 'up':
        y-=amount
        y = min(y,400)
        y = max(y,0)
        return[x,y,direction]
    elif direction == 'down':
        y+=amount
        y = min(y,400)
        y = max(y,0)
        return[x,y,direction]
'''
Turn turns the turtle in  a counter clockwise direction
it outputs the new direction
'''
def turn(x,y,direction):
    if direction == 'right':
            direction = 'up'
            return direction
    elif direction == 'left':
        direction = 'down'
        return direction
    elif direction == 'up':
        direction = 'left'
        return direction
    elif direction == 'down':
        direction = right
        return direction   

'''
starting cooordinates and direction of the turtle
'''

print('Turtle: (200, 200) facing: right')
x = 200
y= 200
direction = 'right'
i=1
commands_entered = []

'''
this loop runs until the user goes 5 times (sleep counts twice)

ask for user input for command and uses .upper to make the comman all uppercase to ensure that case doesnt affect the command

stores command in a list and print list and sorted list at the end of the 5 turns


'''


while i < 6:
    user_input = input('Command (move,jump,turn,sleep) => ')
    print(user_input)
    command = user_input.upper()
    commands_entered.append(user_input)
    if command == 'MOVE':
        (x,y,direction) = move(x,y,direction,20)
        print('Turtle: ({:}, {:}) facing: {:}'.format(x,y,direction))
        i+=1
    elif command == 'JUMP':
        (x,y,direction) = move(x,y,direction,50)
        print('Turtle: ({:}, {:}) facing: {:}'.format(x,y,direction))
        i+=1
    elif command == 'TURN':
        direction = turn(x,y,direction)
        print('Turtle: ({:}, {:}) facing: {:}'.format(x,y,direction))
        i+=1
    elif command == 'SLEEP':
        if i < 5:
            print('Turtle falls asleep.')
            print('Turtle: ({:}, {:}) facing: {:}'.format(x,y,direction))
            print('Turtle is currently sleeping ... no command this turn.')
            print('Turtle: ({:}, {:}) facing: {:}'.format(x,y,direction))
            i+=2
        elif i== 5:
            print('Turtle falls asleep.')
            print('Turtle: ({:}, {:}) facing: {:}'.format(x,y,direction))
            i+=1
            
    else:
        print('Turtle: ({:}, {:}) facing: {:}'.format(x,y,direction))
        i+=1
            
print()
print('All commands entered: {:}'.format(commands_entered))
commands_entered.sort()
print('Sorted commands: {:}'.format(commands_entered))