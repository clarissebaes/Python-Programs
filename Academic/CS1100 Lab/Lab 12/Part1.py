def add(m,n):
    if n == 0:
        return m
    else:
        return add(m,n-1) + 1
    
def mult(m,n):
    if n == 0:
        return n
    if n == 1:
        return m
    if n == -1:
        return -m
    else:

        return add(mult(m,n-1),m)
def power(m,n):
    if n == 0:
        return 1
    if n == 1:
        return m
    if n== -1:
        return 1/m
    else:
        return mult(power(m,n-1),m)
    
        
print(add(5,3))
print(mult(8,3))
print(power(6,4))