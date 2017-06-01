def encrypt(word):
    x = word.replace('a','%4%').replace('he', '7!').replace('e', '9(*9(').replace('y','*%$').replace('u', '@@@').replace('an', '-?').replace('th', '!@+3').replace('o','7654').replace('9','2')
    return print(x)

def decrypt(word):  
    y = word.replace('2','9').replace('7654', 'o').replace('!@+3','th').replace('-?','an').replace('@@@','u').replace( '*%$','y').replace( '9(*9(', 'e').replace( '7!','he').replace('%4%','a')
    return print(y)

print(decrypt('wh*%$ s7654 s2(*2(ri7654@@@s wh*%$ s7654 s2(*2(ri7654@@@s'))

x = input("Enter 'E' for encrypt or 'D' for decrypt ==> ")
if x == 'E' or x == 'e':
    c = str(input('Enter cipher text ==> '))
    print(c)
    print()
    print('Deciphered as ==>', encrypt('c'))
    print('Difference in length ==>', abs(len(c)-len(x))
          