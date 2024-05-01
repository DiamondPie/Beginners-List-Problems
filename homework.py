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
# This method is quite complicated so I fully commented it, but it uses all lists without dictionary to solve this problem.
# I prefer to use collections.Counter() method to solve this problem.

foods = []
for i in range(8):
    ipt = input("What's your favourite food?\n>> ")
    iptInFoods = False # Flag, True if the input option already in foods
    for f in foods:
        if ipt == f[0]: # The input is already in foods
            f.append(ipt) # Add the food again to the list of this kind of food
            iptInFoods = True
            break
    if not iptInFoods: # The input is a new element
        foods.append([ipt]) # Add a list contains 1 of the food to the foodslist
    
times = 0 # most preformed time
mostElements = [] # most time elements, I set a list here to include more than 1 element, i.e. [A, A, B, B, C] contains 2 As and 2 Bs, so A and B should both in mostElements list.
unmostElements = [] # opposite from mostElements

for f in foods:
    if len(f) >= times: 
        # most time elements
        mostElements.append(f[0])
        times = len(f)
    else:
        # un-most time elements
        unmostElements.append(f[0])

# print out the results
for e in mostElements:
    print(e, 'is loved by', times, "people!")
    for _ in range(times):
        print('I love', e)

print('Other foods are:')
for u in unmostElements:
    print(u)

###################### List of (good) Cereals ######################
ipt = ""
cerealList = []
while not ipt.lower() in ['sultana and bran', 'weetbix']:
    ipt = input("Enter cereal\n>> ")
    cerealList.append(ipt)

del cerealList[-1] # remove the last input

print(cerealList)
