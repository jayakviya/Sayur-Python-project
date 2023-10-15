'''
Problem #1
Generate the following output using for loop. Go until g.
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba

look at the output and find the pattern. Hint - add next letter in the alphabet in each row

'''
alphabet = ['a','b','c','d','e','f','g']
alpha =''
for i,value in alphabet:
    print(alphabet[i])
    alpha += chr(ord(alphabet[-1])+1) + alphabet
   
    
    
    
