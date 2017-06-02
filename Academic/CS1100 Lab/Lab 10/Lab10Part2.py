def closest2(listicle):
    difcomp = max(listicle)
    close1 = 0
    close2 = 0    
    listsort = sorted(listicle)
    for i in range(len(listicle)-1):
        dif = abs(listsort[i]-listsort[i+1])
        if dif < difcomp:
            close1 = listsort[i]
            close2 = listsort[i+1]
            difcomp = dif 
    return (close1,close2)

L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
(x,y) = closest2(L1)
print(x,y)
        
        
        
        
          