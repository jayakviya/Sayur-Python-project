########## Program 4 ##########
#PigLatin - From the input string, for each word, remove the first chars until a vowel, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)

inputSentence = input("Enter your input :") #get the input

piglatinkey = "ay" #initialise the key

vowels =["a","e","i","o","u"] #arrange vowels in array
sentence ="" 
outputSentence =[] # to store the output sentence
for word in inputSentence.split(" "): # split the inputsentence and using for llop for every word in the sentece 
    vowelIndex = -1 # intialise to =1 it indicates that no vowels in the word
    
    for index,letter in enumerate(word): #using for and if stm to find out the place of the vowel letter
        if letter.lower() in vowels:
            vowelIndex =  index #to store the index value of the vowel
            break
    if vowelIndex != -1: # if there is a vowel sentence 
             
        sentence = sentence + word[vowelIndex+1:] + word[:vowelIndex+1 ] +piglatinkey + " "
    else:
        sentence = word
outputSentence.append(sentence)  # to add the sentence to output sentence
print("The output sentence is ".join(outputSentence)) # use the key join to print the outputsentence  

'''
output
------
Enter your input :we are just friends
weay reaay stjuay endsfriay '''
