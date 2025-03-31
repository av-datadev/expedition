# ask user their name
# name = input("Whats is your name? ")
# print(f"hello, {name}")

# variables


# Datatypes of variables
# x = 5
# y = 'John'
# print(type(x))


# x = str(3)
# y = int(3)
# z = float(3)
# print(x)
# print(y)
# print(z)

# Case sensitive
# a = 'apoorv'
# A = 'Apoorv'
# print(A)


# Many Values to Multiple Variables
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# One Value to Multiple Variables
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)


# Unpack a Collection
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# # Output Variables
# x = 5
# y = 4
# z = 'John'
# print(x+y,z)


# Global Variables

# x = "awesome"  # Global variable x

# def myfunc():
#     print("Python is " + x)  # Accessing global x

# myfunc()  # Function call

# # Local Variable x Inside Function

# def local_var():
#     x = "good"  # This x is a LOCAL variable (different from the global x)
#     print("Python is " + x)  

# local_var() # Function call

# # Using global x to Modify Global Variable

# def mod_func():
#     global x  # Refers to global x
#     x = "fantastic"  # Changes the global variable

# mod_func()
# print("Python is " + x)


# Strings are Arrays
# a = "Hello, World!"  #this is caled slicing
# print(a[0:6])


# Looping Through a String
# for x in "apple":
#   print(x)

# String Length
# a = "Hello, World!"
# print(len(a))

# check String
# txt = "The best things in life are free!"
# print("sold" in txt)

# txt = "The best things in life are free!"
# if "best" in txt:
#   print("Yes, 'best' is present.")


# check if NOT
# txt = "The best things in life are free!"
# print("expensive" in txt)


# Upper/Lower Case
# a = "Hello, World!"
# print(a.lower())

# Remove Whitespace
# a = ' hello, world '
# print(a.strip())

# Replace String
# a = "Hello, World!"
# print(a.replace("H", "J"))

# Concatenation of string
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# f-string
# age =27
# txt = f'My name is Apoorv, I am {age}'
# print(txt)


# Escape Character \
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# list lenght

# thislist = ["apple", "cherry", "banana", "cherry"]
# print(len(thislist))

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))


# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

#   ative Indexing
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-3])

# Range of Indexes
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])   # this will always return the previous value of the outer range in this case index number 3)


# Range of Negative Indexes
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])


# Check if Item Exists
# thislist = ["apple", "banana", "cherry"]
# if "cherry" in thislist:
#   print("Yes, 'cherry' is in the fruits list")

# Change Item Value
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# Change a Range of Item Values
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[0:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# Insert Items
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# Append List
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# insert list
# thislist = ['apple', 'banana', 'cherry']
# thislist.insert(0,'Orange')
# print(thislist)


# Extend List
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# tropical.extend(thislist)
# print(tropical)

# Add Any Iterable
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# Remove Specified Item
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# remove a specific index
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(0)       # if no index is mentioned it will remove the last item.
# print(thislist)


# using del function
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# Clear the List
# thislist = ['apple', 'banana', 'cherry']
# thislist.clear()
# print(thislist)

# Loop Through a List
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# Loop Through the Index Numbers
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])


# Using a While Loop
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


# Looping Using List Comprehension
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]


# List Comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "e" in x:
#     newlist.append(x)
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "e" in x]
# print(newlist)

# Iterable
# newlist = [x for x in range(10)]

# Sort List Alphanumerically
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)
# to arrage it in descending order use the reverse = True in
# thislist.sort(reverse=True)

# Customize Sort Function
# def myfunc(n):
#   return abs(n - 100)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# Case Insensitive Sort
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# for lower case
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# revrese sorting
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# Copy a List
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

#
# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)


# Join Two Lists
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list2 + list1
# print(list3)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#   list1.append(x)
# print(list1)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)

# TUPLE
# thistuple = ("apple" , "banana" , "oranges")
# print(thistuple)

# SINGLE TUPLE
# thistuple = ("apple",)   #comma is important for single tuple creations
# print(thistuple)

# TUPLE ITEMS
# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
# # print(tuple2+tuple3)
# print(type(tuple1))        # for tuple datatype

# ACCESS TUPLE ITEMS
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-3])

# RANGES OF TUPLE
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])    # 2 is inclusive and 5 is not
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# Change Tuple Values
# x = ("apple" , "banana" , "cherry")
# y = list(x)
# y[0] = "kiwi"
# x = tuple(y)
# print(x)

# ADD ITEMS
# x = ("apple" ,"banana", "cherry")
# y = list(x)
# y.append("kiwi")   # append will take only a singel argument
# x = list(y)
# print(x)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)

# REMOVE ITEM
# thistuple = ("apple","banana","cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = list(y)
# print(thistuple)


# DELETE A TUPLE

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists


# UNPACK A TUPLE
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# Unpacking using an * sign

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, *yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# LOOP THROUGH A TUPLE
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)

# LOOP THROUGH INDEX NUMBER
# thistuple = ("apple", "banana", "cherry" , "orange")
# for i in range(len(thistuple)):
# print(thistuple[i])

# USING A WHILE LOOP
# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

# MULTIPLY A TUPLE
# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
# print(mytuple)


# SETS
# they are unordered , unchangble and no duplicates are allowed

# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)

# thisset = {"apple", "banana", "cherry", False, 0, 2}   # TRUE = 1 and FALSE = 0 only the boolean is printed
# print(thisset)

# thisset = {"apple", "banana", "cherry","apple"} # duplicate does not count
# print(len(thisset))

# TYPE of SETS
# myset = {"apple", "banana", "cherry"}
# print(type(myset))

# set constructor
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# Access Items in set
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# thisset = {"apple", "banana", "cherry"}
# print("banana" not in thisset)

# UPDATING A SET
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

# Add any iterables
# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)

# Remove/Discard Item
# thisset = {"apple" , "banana", "cherry"}
# thisset.discard("banana")       # if the item to be removed is not present in the set the remove will show an error and discard will not.
# print(thisset)

# using the POP function
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)

# Empty a set
# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)

# Loop in sets
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)


# Joining sets
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1 | set2  # use of | operator
# print(set3)

# Join multiple sets
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = set1.union(set2, set3, set4)
# print(myset)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = set1 | set2 | set3 |set4
# print(myset)

# joining a set and a tuple

# x = {"apple", "banana", "cherry"}
# y = (1,2,3)
# z = x.union(y)
# print(z)

# updating a set

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)

# intersection or &

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)   # this looks for the commom item in the set
# print(set3)

# Note: The & operator only allows you to join sets with sets, and not with
# other data types like you can with the intersection() method.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2
# print(set3)

# interaction_update()
# The intersection_update() method will also keep ONLY the duplicates,
# but it will change the original set instead of returning a new set.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.intersection_update(set2)
# print(set1)

# The values True and 1 are considered the same value. The same goes for False and 0.
# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
# set3 = set1.intersection(set2)
# print(set3)

# Difference or (-)
# The difference() method will return a new set that will contain only the items
# from the first set that are not present in the other set.

# Note: The - operator only allows you to join sets with sets,
# and not with other data types like you can with the difference() method.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2) OR set3 = set1 - set2
# print(set3)

# difference_update()
# The difference_update() method will also keep the items from the first set that are not in the other set,
# but it will change the original set instead of returning a new set.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1)

# Symmetric Differences or ^

# Note: The ^ operator only allows you to join sets with sets,
# and not with other data types like you can with the symmetric_difference() method.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1^(set2)
# print(set3)


# CS50

# ask user's name         ---- mention input wif you want any input from the user.
# name = input("What is your name? ").strip().title()
# #split the user's name
# first = name.split(" ")
# # say hello to user
# print(f"hello, {name}")
