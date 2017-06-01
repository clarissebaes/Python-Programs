'''
reverse 3 digit number
'''
def reverse3(x):
    hund = x//100
    tens = (x%100)//10
    ones = (x%100)%10
    return (int((ones * 100) + (tens*10) + hund))
'''
reverse 5 digit number
'''
def reverse5(y):
    first_3 = (y//100)
    last_2 = (y%100)
    ten_thous = last_2//10
    thous = last_2%10
    final_3 = (reverse3(first_3))
    return ten_thous * 1000+ thous * 10000 + final_3

print('Enter a 5 digit number whose first and third digits must differ by at least 2.')
print('The answer will be 1089, if your number is valid')
a = int(input('Enter a value ==> '))
print(a)
b = reverse5(a)
print()
print('Here is the computation:')
print(a, 'reversed is', int(b))

'''
take first 3 of original number(f3org) and last 3 of reversed (l3rev)
and subtract smaller(small) from larger(large) = new_num
'''
f3org = a//100
l3rev = b%1000
small = min(f3org,l3rev)
large = max(f3org,l3rev)
new_num = large-small
print(large,'-',small,'=',new_num)

'''
add new_num to reversed new_num
'''
rev_new = reverse3(new_num)

final_ans = new_num + rev_new

print(new_num, '+', rev_new, '=', final_ans)
print('You see, I told you.')