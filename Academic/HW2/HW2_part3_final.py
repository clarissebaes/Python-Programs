'''
encryption function
'''
def encrypt(word):
    x = word.replace(' a','%4%').replace('he', '7!').replace('e', '9(*9(').replace('y','*%$').replace('u', '@@@').replace('an', '-?').replace('th', '!@+3').replace('o','7654').replace('9','2')
    return x
'''
decryption function
'''
def decrypt(word):  
    y = word.replace('2','9').replace('7654', 'o').replace('!@+3','th').replace('-?','an').replace('@@@','u').replace( '*%$','y').replace( '9(*9(', 'e').replace( '7!','he').replace('%4%',' a')
    return y


x = input("Enter 'E' for encrypt or 'D' for decrypt ==> ")
print(x)

'''
user inputs e/E for encryption then use encryption 
user inputs d/D use decryption function
anything else results in error message

'''
if x == 'E' or x == 'e':
    reg_text = (input('Enter regular text ==> '))
    print(reg_text)
    enc = encrypt(reg_text)
    print()
    print('Encrypted as ==>', enc)
    print('Difference in length ==>', abs(len(reg_text)-len(enc)))

elif x == 'D' or x =='d':
    code = str(input('Enter cipher text ==> '))
    print(code)
    dec = decrypt(code)
    print()
    print('Deciphered as ==>', dec)
    print('Difference in length ==>', abs(len(code)-len(dec)))    
else:
    print("I didn't understand ... exiting")