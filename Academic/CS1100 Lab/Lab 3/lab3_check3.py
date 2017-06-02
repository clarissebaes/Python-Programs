x = int(input('Number of bunnies ==> '))
print(x)
y = int(input('Number of foxes ==> '))
print(y)

def next_bpop(bpop,fpop):
    bpop_next = (10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop    
    bpop_new = int(bpop_next)
    return bpop_new

def next_fpop(bpop,fpop):
    fpop_next = max((0.4 * fpop + 0.02 * fpop * bpop), 0)
    fpop_new = int(fpop_next)
    return fpop_new


print('Year 1:', int(x), int(y))
bpop_new = next_bpop(x,y)
fpop_new = next_fpop(x,y)
print('Year 2:', int(bpop_new), int(fpop_new))
bpop_new1 = next_bpop(bpop_new, fpop_new)
fpop_new = next_fpop(bpop_new, fpop_new)
bpop_new = bpop_new1
print('Year 3:', int(bpop_new), int(fpop_new))
bpop_new1 = next_bpop(bpop_new, fpop_new)
fpop_new = next_fpop(bpop_new, fpop_new)
bpop_new = bpop_new1
print('Year 4:', int(bpop_new), int(fpop_new))
bpop_new1 = next_bpop(bpop_new, fpop_new)
fpop_new = next_fpop(bpop_new, fpop_new)
bpop_new = bpop_new1
print('Year 5:', int(bpop_new), int(fpop_new))