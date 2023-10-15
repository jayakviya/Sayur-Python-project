#From a given passage extract unique words and print them.
# Accept the passage as an input from the user

passage = input("Enter your passage:")
words = passage.split()

uniqueWord = set(words)
print("The unique words n the passage are,")

for word in uniqueWord:
    print(word)

print(f"The no of unique words is {uniqueWord.__len__()}")
'''
output 1:
PS C:\Users\DELL\Documents\Sayur-Python-project-2> & "C:/Program Files/Python311-32/python.exe" "c:/Users/DELL/Documents/Sayur-Python-project-2/programs/From a given passage extract unique word.py"
Enter your passage:Apples are a versatile and beloved fruit enjoyed by people of all ages around the world. They are not only delicious but also a healthy addition to a balanced diet.
The unique words n the passage are,
around
balanced
They
to
only
ages
also
diet.
world.
healthy
Apples
and
but
fruit
enjoyed
versatile
a
the
of
people
delicious
by
are
all
not
beloved
addition
The no of unique words is 27
'''