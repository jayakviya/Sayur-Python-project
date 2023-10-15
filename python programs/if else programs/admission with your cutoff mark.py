sum =0
for i in range(1,6):
    mark = int(input(f"Enter you mark in subject {i} ="))
    sum = sum +mark
print("Total mark=",sum)
avg = sum/5
print("Average=",avg)
'''
cut off marks of 3 colleges
college 1 - 88%
college 2 - 96%
college3 - 90%
'''
if avg >= 96:
    print("You are eligible for admission in all three colleges")
elif avg >= 90:
    print("You are eligible for admission in college 1 and college 3")
elif avg >= 88:
    print("You are eligible for admission in college 1")
else :
    print("Tou are not eligible for admission in these three colleges")