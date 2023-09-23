############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like

#init variables
movies = input("What movies you like ? ")
#convert movies into a List
movies = movies.split(" ")
print(movies)
commonMoviewCount = 0
while (True) :
    #ask the second friend for one movie at a time
    movie = input ("Tell me your favourite movie?" )
    #Check if this movie is in the movie list
    #FillinMissingCode
    if movie in movies: 
        commonMoviewCount += commonMoviewCount+1
    #check if we reached the max
    if(commmonMovieCount >= 3):
        break
    else:
        print ("Try again")

print () #FillinMissingCode - list all the common movies

