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
    
# TUples are similar to array but are immutable in python 
tup = (1,2,3)

can't modify them
tup[0] = 2 # this will give an error

You are mainly using tuuple  for  a key to hashman / set because they are immutable and hashable in python  
mymap = {(1,2) : 3} # this is valid because the key is a tuuple and tuuple is immutable and hashable in python  
mySet  = set((1,2)) # this is valid because the key is a tuuple and tuuple is immutable and hashable in python  

my[[1,2]] = 3 # this is invalid because the key is a list and list is mutable and unhashable in python  

#Heaps
# Heap is a binary tree where the parent node is smaller than the child node in min heap and parent node is greater than the child node in max heap
import heapq
under the hood heapq is implemented using a list in python and it is a min heap by default
minHeap = [3, 1, 4, 1, 5]
heapq.heapify(minHeap)
heapq.heappush(minheap, 2)
heapq.heappop(minHeap) # this will pop the minimum element from the heap

# minimum values is always at the index 0 of the heap
print(mineHeap[0])
while(len(minHeap) > 0) :
    print(heapq.heappop(minHeap)) # this will pop the minimum element from the heap

# python does not have a max heap by default but we can implement it using a min heap by negating the values
maxHeap = []
for x in [3, 1, 4, 1, 5]:
    heapq.heappush(maxHeap, -1 * x)
while maxHeap:
    print(-1 * heapq.heappop(maxHeap))

# Functions
# Funcions are first class citizens in python, we can pass them as arguments to other functions and return them from other functions
# use def key workword, name the function , 
and then we pass in some parameter just like conditions
 and loops we use : after the declaration of the function and
  then we write the body of the function
def myFunct(int a, int  c):
    return math.sqrt(a * a + c * c)

one function property that is mostly used in coding interview is inner funtion
def outerFunct(int a, int b):
    def innerFunct(int c):
        return a + b + c
    return innerFunct
print(outerFunct(1, 2)(3)) # this will print 6 because the inner function is called with the argument 3 and the outer function is called with the arguments 1 and 2
in graph it is very useful to use inner function because we can use the outer function variables in the inner function without passing them as arguments to the inner function
# graph example
def graphDFS(int node, int parent):
    def dfs(int node, int parent):
        for neighbor in graph[node]:
            if neighbor != parent:
                dfs(neighbor, node)
    dfs(node, parent)
graphDFS(0, -1) # this will start the dfs from node 0 and parent -1


# can modify the objects but  not reassign variable 
# unless using non local keyword
def double(arr, val):
    for i in range(len(arr)):
        arr[i] *= 2
    val *= 2
    # this will not modify the val variable because it is a local variable and it is not passed by reference
    nonlocal val # this will modify the val variable because it is a nonlocal variable and it is passed by reference
    val *= 2


# class
Class Are also pretty concise but a bit more limited as compared to other languages like java and c++
 but they are still pretty powerful

 class myClass:
    #construction of the class is done using __init__ method
    # self is passed to every method of class and it is used to access the instance variables of the class
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def myMethod(self):
        return self.a + self.b
    # call other memeber function of the class using self keyword
    def myMethod2(self):
        return self.myMethod() * 2

# to create member variable we use self keyword and to access the member variable we use self keyword as well

# here is the table that comapre python with other languages like java and c++
#create the table that compare python with other languages like java and c++
features = ["Syntax", "Data Types", "Memory Management", "Performance", "Community Support"]
python = ["Simple and readable", "Dynamically typed", "Automatic memory management", "Moderate performance", "Large community"]

java = ["Verbose and strict", "Statically typed", "Manual memory management", "High performance", "Large community"]
cpp = ["Complex and strict", "Statically typed", "Manual memory management", "High performance", "Large community"]
c = ["Complex and strict", "Statically typed", "Manual memory management", "High performance", "Large community"]

# oops concept compare python with other languages like java and c++
# compare various ways to implement oops concept in python with other languages like java and c++

python is dyanamically typed and interpreted language, while java and c++ are statically typed and compiled languages. Python supports multiple inheritance, while java supports single inheritance and c++ supports multiple inheritance. Python uses duck typing, while java and c++ use static typing. Python has a garbage collector, while java has a garbage collector and c++ does not have a garbage collector. Python has a large standard library, while java has a large standard library and c++ has a small standard library.
pythone is interpreteted languge, users code converted to bytecode and then executed by the python interpreter, while java is compiled to bytecode and then executed by the java virtual machine and c++ is compiled to machine code and then executed by the operating system. Python is dynamically typed, while java and c++ are statically typed. Python supports multiple inheritance, while java supports single inheritance and c++ supports multiple inheritance. Python uses duck typing, while java and c++ use static typing. Python has a garbage collector, while java has a garbage collector and c++ does not have a garbage collector. Python has a large standard library, while java has a large standard library and c++ has a small standard library.
