def is_alternating(word):
        if word[0]  not in vowels: #this checks if the word starts with a vowel 
                return False        
        elif len(word) < 8: #makes sure that the word is at least 8 letters long
                return False
        else:
                t = 0
                for i in range(0,(len(word)-2),2): #the range out puts every other even number so that it checks if it is alternating vowel and consonants
                        if word[i] in vowels and word[i+1] in consonants: 
                                t+=0 #if its a vowel followed by a consotant t remains 0 and true is outputted
                        else:
                                t += 1 #if its not a consonant it has to be a vowel and 1 is added to t. Since T is greater than 0 False is outputted
                for i in range(1,(len(word)-2),2): # same range as before but since it is checking only yht consonants it starts at 1 instead of 0
                        if word[i] < word[i+2]:# this make sure that the consonants are increasing alphabetically
                                t += 0
                        else:
                                t += 1
                
                if t > 0 :
                        return False
                elif t == 0 :
                        return True

#main code starts here


vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

        
user_input = input('Enter a word => ')
word = user_input.lower()
print(user_input)

output = is_alternating(word)

if output is True:
        print("The word '{:}' is alternating".format(user_input))
elif output is False:
        print("The word '{:}' is not alternating".format(user_input))        



