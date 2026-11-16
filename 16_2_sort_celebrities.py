# import the sorting module
# make sure it doesn't output the test code there!
import sorts

#Each list has [name, age, # of movies]
celebrities_list = [["Tom Cruise", 58, 47], ["Jennifer Lawrence", 31, 25], 
                    ["Dwayne Johnson", 49, 57], ["Scarlett Johansson", 37, 48], 
                    ["Chris Hemsworth", 38, 32], ["Leonardo DiCaprio", 47, 46], 
                    ["Angelina Jolie", 46, 44], ["Brad Pitt", 58, 49], 
                    ["Emma Watson", 31, 21], ["Robert Downey Jr.", 56, 63], 
                    ["Meryl Streep", 72, 81], ["Will Smith", 53, 52], 
                    ["Anne Hathaway", 38, 39], ["Johnny Depp", 58, 52], 
                    ["Cate Blanchett", 52, 64], ["Matt Damon", 51, 63], 
                    ["Charlize Theron", 45, 46], ["Hugh Jackman", 53, 38], 
                    ["Jennifer Aniston", 52, 38], ["George Clooney", 60, 57]]

# sort the celebrities by age using selection sort
selectionCelebrities = sorts.selection_sort(celebrities_list, 1)
for celebrity in selectionCelebrities:
    print(celebrity)
print()
# sort the celebrities by number of movies made using insertion sort
insertionCelebrities = sorts.insertion_sort(celebrities_list, 2)
for celebrity in insertionCelebrities:
    print(celebrity)

