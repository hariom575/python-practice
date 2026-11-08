# Newton School Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello from Newton School! 👋")
n, m = 0 , "abc"
print(n)
print(m)

# n++ 
n = n + 1 
n+=1
print(n)
# n++ bad in python
# We don't need curly braces in python an  python interpreter if and else 

# logical && = and, or ||
# condition is not written in parenthesis in python it is written in open form like while i <  5 : not while (i < 5)
# None : Absense of a value

# For loop
# for i in range (5) i is increamented annd 5 is not included 
# for i in range(2, 5) : 2 to 4
# for i in range (2, 5 , -1) this is decreament the i  you can also pass -2  if you decreament by 2
# for (int i = 0; i < n; i++)

# 5/2 this is float division 
# 5//2 this is the integer devision 
# Most language round down towards 0 
# print(-3 / 2) will print -2
# a work arount this is print(int(-3 / 2))
# every thing is object in python
# print(10 % 3) reminder issue is negative 
# except for negative value
# import math
# print(math.fmod(-10, 3))
# math.floor(3/2)
math.ceil(3/2)
math.sqrt(2)
math.pow(2, 3)
float("inf") # max value
float("-inf") # min value
import math
math.pow(2, 2000) < float(inf)

# Array is called list in python
arr = [1, 2, 3]
# Array in are dynamic array by default
arr.append(4)
arr.append(5)
arr.pop()

# we can actually insert in the middle
arr.insert(1,  7) # o(n) time 

n = None
print(n)


# indexing the array is constant time operation like arr[0] or arr[n - 1]

# Initialize an arry of variable size with the some value|
arr = [1] * n # created an array of n and intialized it with 1

print(arr) # you can directly print the whole array in python unlick other langauge
print(len(arr)) # you can print len of the array like this
print(arr[-1]) # not out of bound in python you can read the values from last to first using negative index
print(arr[1 : 3]) # slicing in python

# unpacking 
a, b,c = [1, 2, 3] # you can take all the individual elements from the array and assign them to every variable a, b,c
print(a, ,b,c) # you can print multiple values like this
# Be careful though 
# a, b = [1, 2, 3] wont work because the no of elements that you are expecting from the array should match the no. of elements that you are getting from the array
# Loop through the array
for i range(len(arr)) :
    print(arr[i])

# Without index
for n in nums : 
    print n
for i, n in enumerate(nums) :
    print(i , n)  # the first value is index and second value is the value itself
# Iterate through multiple  array simulataneously we can do it with unpacking and a helper fuction called zip
for n1,  n2 in zip(nums1, nums2) :
    print(n1, n2) # pair of n1, n2
nums.reverse() # to reverse() the array
nums.sort() # to sort the array
arr.sort(reverse = True) # descending order
arr = ["bob", "alice", "doe"]
arr.sort() # sort it based on alphatical order
# custom sort by len of string
arr.sort(key = lamda x : len(x))

# List Comprehension
arr = [i for i in range(5)] # this is List Comprehension


# you can do any silly stuff as well
arr = [ i + 1 for i in range(5)]

# 2D list
arr = [[0] * 4 for i in range(4)]

# a 4 by 4 ka thela
arr = [[0] * 4] * 4 # this is bakchodi, you should not do this because it will create four copy of the same array row, and if you modify the single row it is gonnna modify every row
# we are not creating 4 unique row 
s = "abc"
# slice them in same way a array
# string is immmutable in python

# we can append someting , so anytime if we append anything it is goint to create a new string , so updating a string is n time operation in python
s+="abc" # it is going to create a new string 
# Valid numeric string can be converted
print(int("123") + int("43"))
print(str(123) + str(24)) # integers can also be converted to string append the strings
# to get the asci value oof string do the following bitch or of a characted
print(ord("a"))

# combine a list of string with a delimiter  (with a empty string)
strings = ["ab",  "bc", "cd"]
print(",".join(strings))
q = deque() # q in python are simply double ended q in python
q.append(1)
q.popleft() # constant time operation
q.appendleft(1) # constatn time operation to insert anything on the left side
q.pop() # pop from the right side

# hash set are very useful  we can search and and add value in constant time

mySet = Set()
mySet.add(1)
mysSet.add(1)
# there can not be any duplicate in the hashset
print(len(myset)) # this mother fucker will print the lenght of the hashset
print(1 in hasset) # to search this in hashset 
2 in haset 
hashset.remove(2) # to remove the value from hashset
# list to set
print(set([1, 2, 3]))

# Set comprehension
myset = {i for in range(5)}

# HashMap aka dict
myMap = {}
myMap["alice"] = 16 
print(len(mymap))
print (alice in mymap)

# remove mymap.remove("alice")
myMap = {"alice" : 80, "hd" : 809}

# Dict comprehension
mapp = {i : 2 * i  for i range(3)}

# iterate over map
for key in map:
    print(key, map[key])
# we can directly iteratee over values if we don't need the key

for val in map.values() :
    print(val)
for key, val  in myMap.items() :
    
