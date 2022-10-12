# Write a program to count how many times a no. is repeated in list

# the function which will help us to find no. of times an item is repeated
def countX(list, x):
    count = 0
    for i in list:
        if (i == x):
            count = count + 1
    return count
 
 
# the list in which we need to find the elemnt 
list = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# the no. which we need to find occurence in the list
x = 1
print(x, "has occured", countX(list, x), "times")
