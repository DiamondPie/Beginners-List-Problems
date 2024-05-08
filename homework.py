### The comments are worth a look, aren't they? =) ###

###################### Starter ######################
numsList = [7, 6, 23, 8.18, 18, 8, 7.2, 85, 915, 12]

maxnum = max(numsList)
print("biggest", maxnum)
print("biggest number at", numsList.index(maxnum))
minnum = min(numsList)
print("smallest", minnum)
print("smallest number at", numsList.index(minnum))
print("average", sum(numsList)/len(numsList)) # avg(x) = Σx/n

###################### Same Start and End ######################
stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]
print([string for string in filter(lambda x: x[0].lower() == x[-1].lower(), stringsList)])
# I use list comprehension because this is the simplest and fastest way to do this.
# Conclusion: for each element in stringsList, filter the string that has the same beginning (which is string[0]) and ending (which is string[-1]) and store them to a new list (the list is temporary -- it is in the print() function)
# The `lambda x: x[0].lower() == x[-1].lower()`, which is a lambda expression, defines an anonymous function, which compares the beginning and the ending and outputs the result, in order to maximizly simplify the code

###################### I Like Pesto ######################
foodList = []
count = 0
for _ in range(8):
    food = input("What's your favourite food?").lower()
    if food == "pesto":
        count += 1
    else:
        foodList.append(food)

print(count, "people love pesto")
for _ in range(count):
    print("I love pesto")
    
###################### List of (good) Cereals ######################
ipt = ""
cerealList = []
while not ipt.lower() in ['sultana and bran', 'weetbix']:
    ipt = input("Enter cereal\n>> ")
    cerealList.append(ipt)

del cerealList[-1] # remove the last input

print(cerealList)
