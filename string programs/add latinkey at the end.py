########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

inputsentence = input("Enter your sentence :")#get the input
piglatinKey = "ay" # initialise the key letter
sentence = ""
for word in inputsentence.split(" ") : # this loop execute the no of words in the input sentence
    firstLetter = word[0]
    sentence = sentence + word[1:] + firstLetter + piglatinKey + " "
print("_"*30)
print("The changed sentence = ",sentence)
print("_"*30)
'''
The Output is 
Enter your sentence :We are friends
______________________________
The changed sentence =  eWay reaay riendsfay
'''
