########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

inputsentence = input("Enter your sentence")#get the input
piglatinKey = "ay" # initialise the key letter
sentence = ""
for word in inputsentence.split(" ") : # this loop execute the no of words in the input sentence
    sentence = sentence + word[1:] + word[0] + piglatinKey
print("The changed sentence = ",sentence)
print("_"*10)


