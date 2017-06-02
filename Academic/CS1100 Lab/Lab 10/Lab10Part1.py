def closest1(listicle):
    if len(listicle)<2:
        x = 'None'        
        return (x,x)
    else:
        difcomp = max(listicle)
        close1 = 0
        close2 = 0
        for num1 in range(len(listicle)):
            for num2 in range(len(listicle)):
                dif = abs(listicle[num1]-listicle[num2])
                if num1 != num2:
                    if dif <difcomp:
                        close1 = listicle[num1]
                        close2 = listicle[num2]
                        difcomp = dif
        return (close1,close2)
                
                
                
L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
(x,y) = closest1(L1)
print(x,y)