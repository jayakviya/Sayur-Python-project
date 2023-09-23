############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like

#init variables
movies = input("What movies you like ? ")
#convert movies into a List
movies = movies.split(",")
matchingMovie = []
commonMovieCount = 0
while (True) :
    #ask the second friend for one movie at a time
    movie = input ("Tell me your favourite movie?" )
    #Check if this movie is in the movie list
    #FillinMissingCode
    if movie in movies: 
        commonMovieCount+=1
        matchingMovie.append(movie)

    #check if we reached the max
    if(commonMovieCount >= 3):
        break
    else:
        print ("Try again")

print ()

print(" ".join(matchingMovie))