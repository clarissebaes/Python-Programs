bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]


def printboard(listicle):
    print('---------------------------------')
    for row in range(len(bd)):    
        if (row+1)%3 == 0:
            bd[row].insert(3,'|')
            bd[row].insert(7,'|')
            outgrid = str(bd[row]).replace("'",'').replace('[','|').replace(']', '|').replace(',',' ')
            print(outgrid)
            print('---------------------------------')
        else:
            bd[row].insert(3,'|')
            bd[row].insert(7,'|')        
            outgrid = str(bd[row]).replace("'",'').replace('[','|').replace(']', '|').replace(',',' ')
            print(outgrid) 
            
            
in_row = int(input('Enter a Row => '))
if in_row < 0 or in_row > 9:
    print('invalid')
    sys.exit
print(in_row)
in_col = int(input('Enter a Column => '))
if in_col< 0 or in_col > 9:
    print('invalid')
    sys.exit
print(in_col)
in_num = (input('Enter a Number => '))
if int(in_num) < 0 or int(in_num) > 9:
    print('invalid')
    sys.exit
print(in_num)



def ok_to_add( listicle, row, col, num):
    rownum = int(row)
    colnum = int(col)
    numnum = int(num)
    t= 0
    for rowzz in range(len(listicle)):
        if num == listicle[rowzz][col]:
            t+=1
    if num in listicle[row]:
        t+=1
    elif rownum >=0 and rownum <=2:
        if colnum>=0 and colnum <=2:
            for rowzz in range(2):
                for colzz in range(2):
                    if num == listicle[rowzz][colzz]:
                        t+=1
        if colnum >=3 and colnum <=5:
            for rowzz in range(2):
                for colzz in range(3,5):
                    if num == listicle[rowzz][colzz]:
                        t+=1
        if colnum >=6 and colnum <=8:
            for rowzz in range(2):
                for colzz in range(6,8):
                    if num == listicle[rowzz][colzz]:
                        t+=1
                        
    elif rownum >=3 and rownum <=5:
        if colnum>=0 and colnum <=2:
            for rowzz in range(3,5):
                for colzz in range(2):
                    if num == listicle[rowzz][colzz]:
                        t+=1
                        
        if colnum >=3 and colnum <=5:
            for rowzz in range(3,5):
                for colzz in range(3,5):
                    if num == listicle[rowzz][colzz]:
                        t+=1
                        
        if colnum >=3 and colnum <=5:
            for rowzz in range(3,5):
                for colzz in range(6,8):
                    if num == listicle[rowzz][colzz]:
                        t+=1
                        
    elif rownum >=6 and rownum <=8:
        if colnum>=0 and colnum <=2:
            for rowzz in range(6,8):
                for colzz in range(2):
                    if num == listicle[rowzz][colzz]:
                        t+=1
                        
        if colnum >=3 and colnum <=5:
            for rowzz in range(6,8):
                for colzz in range(3,5):
                    if num == listicle[rowzz][colzz]:
                        t+=1
                        
        if colnum >=6 and colnum <=8:
            for rowzz in range(6,8):
                for colzz in range(6,8):
                    if num == listicle[rowzz][colzz]:
                        t+=1
                        
    return t

        




x = (ok_to_add(bd,in_row,in_col,in_num))
print(x)
if x == 0:
    bd[in_row][in_col] = in_num
    printboard(bd)
elif x>0:
    print('This is not a valid input')
