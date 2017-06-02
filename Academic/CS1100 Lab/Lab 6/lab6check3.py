def printboard(listicle):
    print('---------------------------------')
    for row in range(len(listicle)):    
        if (row+1)%3 == 0:      
            listicle[row].insert(3,'x')
            listicle[row].insert(7,'x')            
            outgrid = str(listicle[row]).replace('|','').replace('x','|').replace("'",'').replace('[','|').replace(']', '|').replace(',',' ')
            listicle[row].remove('x')   
            listicle[row].remove('x')
            print(outgrid)
            print('---------------------------------')
        else:
            listicle[row].insert(3,'x')
            listicle[row].insert(7,'x')        
            outgrid = str(listicle[row]).replace('|','').replace('x','|').replace("'",'').replace('[','|').replace(']', '|').replace(',',' ')
            listicle[row].remove('x')
            listicle[row].remove('x')
            print(outgrid) 
            
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

def verify(listicle):
    s=0
    for row in range(len(listicle)):
        if '.' in listicle[row]:
            s +=1
            return(False)
        else:
            s+=0
    for row in range(len(listicle)):
        for col in range(len(listicle[row])):
            if ok_to_add(listicle,row,col,listicle[row][col]) == 1:
                s+=1
            elif ok_to_add(listicle,row,col,listicle[row][col]) == 0:
                s+=0    
    
    if s>0:
        return (False)
    elif s== 0:
        return (True)
    

import lab06_util


in_file = input('Enter file name => ')
listicle = lab06_util.read_sudoku(in_file)
keep_going = verify(listicle)
printboard(listicle)
i=1
while i > 0:
    printboard(listicle)
    keep_going = verify(listicle)
    if keep_going == False:
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
        x = ok_to_add(listicle, in_row, in_col, in_num)
        print(x)
        if x == 0:
            print('111')
            listicle[in_row][in_col] = in_num
            keep_going = verify(listicle)

    elif keep_going == True:
        print('Board is solved')
        i=-1


