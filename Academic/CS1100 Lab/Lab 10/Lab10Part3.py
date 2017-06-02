import time
import random
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

if __name__ == '__main__':
    list100 = []
    for i in range(100):
        x = random.uniform(0.0, 1000.0)
        list100.append(x)
    s1 = time.time()
    tup1 = closest1(list100)
    t1 = time.time() - s1
    s2 = time.time()
    tup2 = closest2(list100)
    t2 = time.time() - s2    
    
    print("100 list {}: closest1 time {} and  closest2 time {}".format(tup1, t1,t2)) 
    
    list1000 = []
    for i in range(1000):
        x = random.uniform(0.0, 1000.0)
        list1000.append(x)
    s1 = time.time()
    tup1 = closest1(list1000)
    t1 = time.time() - s1
    s2 = time.time()
    tup2 = closest2(list100)
    t2 = time.time() - s2    
    
    print("1000 list {}: closest1 time {} and  closest2 time {}".format(tup1, t1,t2)) 
    
    list10000 = []
    for i in range(10000):
        x = random.uniform(0.0, 1000.0)
        list10000.append(x)
    s1 = time.time()
    tup1 = closest1(list10000)
    t1 = time.time() - s1
    s2 = time.time()
    tup2 = closest2(list100)
    t2 = time.time() - s2    
    
    print("10000 list {}: closest1 time {} and  closest2 time {}".format(tup1, t1,t2))    
    