'''
problem #4
write a program to find if two strings are same.
two string are considered same if both strings have same letters in same order, but from different starting point
eg abcd is same as bcda (a is moved to the right)
abcd is same as cdab 
abcd is  not same as cdba

123456 = 456123
123456 not = 412356
hint - 
there are many simple answers. you can try with slice function'''

def are_strings_same(string1, string2):
    # Check if the lengths of the strings are the same
    if len(string1) != len(string2):
        return False

    sliced_string1 = string1[:len(string1)//2]
    sliced_string2 = string1[len(string1)//2:]
    con_string = sliced_string2 + sliced_string1

    # Check if string2 is a substring of the concatenated string
    if (string2 == con_string) or (string1 == string2):
        return True
    else:
        return False

# Test the function
string1 = list(input("Enter the first string :"))
string2 = list(input("Enter the second string :"))
result = are_strings_same(string1, string2)
string1 = ''.join(string1)
string2 = ''.join(string2)
if result:
    print(f"{string1} and {string2} are the same.")
else:
    print(f"{string2} and {string2} are not the same.")