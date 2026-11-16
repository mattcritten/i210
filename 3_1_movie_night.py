## 3.3 Movie night

# Meet the dad. He owns several favorite movies. Some he likes so much he has multiple copies.
dad_movies = ["Die Hard", "Jaws", "Alien", "Princess Mononoke", "Die Hard", "Alien", "Jurassic World"]

# Meet the kid. He also owns some favorite movies.
kid_movies = ["Jurassic World", "Princess Mononoke", "Dragonball Z", "Kung Fu Panda", "How to Train Your Dragon"]

#1 Make each movie list only contain one copy of each movie by transforming them into sets
dad_set = set(dad_movies)
kid_set = set(kid_movies)

#2 What movies do the dad and kid have to select from? (List all movies in either list)
print(dad_set.union(kid_set))

#3 What movies are liked by either the dad or the kid, but not both?
print(dad_set.symmetric_difference(kid_set))

#4 What movies does only the dad like?
print(dad_set.difference(kid_set))

#5 What movies do both the dad and the kid like?
 

# (Still have two choices for movie night! Hope they can agree on one. ;-)
