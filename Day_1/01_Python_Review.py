
# coding: utf-8

# ## Python Crash Course
# ### Reference: 
# https://www.tutorialspoint.com/python/

# ## 1. The syntax of the if...else statement is 

# 
# if expression:
#    statement(s)
# else:
#    statement(s)

# In[3]:


value = True
if value:
   print("Got a true expression value ",value)
else:
   print("Got a false expression value ",value)


# ## 2. The syntax of the elif Statement

# if expression1:
#    statement(s)
# elif expression2:
#    statement(s)
# elif expression3:
#    statement(s)
# else:
#    statement(s)

# In[6]:


value = 150
if value == 200:
   print("value is 200")
elif value == 150:
   print ("value is 150")
elif value == 100:
   print ("value is 100")
else:
   print ("value is not (100,150,200)")
print("End!")


# ## 3. The syntax of the for Statement

# for iterating_var in sequence:
#    statements(s)

# In[7]:


for letter in "Python":
   print (letter)


# In[8]:


fruits = ["banana", "apple",  "mango"]
for fruit in fruits:        
   print (fruit)


# In[9]:


fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print(fruits[index])


# ## 4. The syntax of the while Statement

# while expression:
#    statement(s)

# In[56]:


count = 0
while (count < 9):
   print('The count is:', count)
   count = count + 1


# ## 5. Python Lists
# The most basic data structure in Python is the sequence. Each element of a sequence is assigned a number - its position or index. The first index is zero, the second index is one, and so forth.

# <li> An ordered group of items
# <li>Does not need to be the same type
# <li>Could put numbers, strings or objects in the same list
# <li>List notation
# <li>A = [1,”This is a list”, c, Donkey(“kong”)]

# In[11]:


list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]


# In[17]:


for x in list1:
    for y in list2:
        print(x, y)


# ### Accessing Values in Lists

# In[28]:


list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [0, 1, 2, 3, 4, 5, 6 ];
print("list1[1]: ", list1[1])
print("list2[1:3]: ", list2[1:3])
del list1[2] #Delete element in a list
print (list1[0:3])
list1[2]=2001 #Change element in a list
print (list1[0:3])


# ### Updating Lists

# In[64]:


list = ['physics', 'chemistry', 1997, 2000];
print("Value available at index 2 : ", list[2])
list[2] = 2001;
print("New value available at index 2 : ", list[2])


# ### Delete List Elements

# In[67]:


list = ['physics', 'math', 1997, 2000];
print(list)
del list[2]
print("After deleting value at index 2 : ")
print (list)


# ### Basic List Operations
# Lists respond to the + and * operators much like strings;

# In[73]:


list = ['physics', 'math', 1997, 2000];
print (len(list))
list = list + ["AI", 2018]
print (list)
print (list*2)


# ## 6. Tuples
# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

# In[78]:


tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
print(type(tup3))


# ### Accessing Values in Tuples

# In[86]:


tup1 = ('physics', 'chemistry', 1997, 2000)
print (len(tup1))
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])


# #### Tuples are immutable which means you cannot update or change the values of tuple elements. 

# In[84]:


tup1[0] = 100


# ## 7.0 Python Set
# A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.

# In[32]:


normal_set = set([1, "b","c"])
print(normal_set)


# In[33]:


normal_set.add("d")
print(normal_set)


# In[34]:


normal_set.add("d")
print(normal_set)


# ## 8.0 Python Dictionary
# Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}.

# In[87]:


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])


# ### Updating Dictionary

# In[94]:


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
print (dict)


# In[96]:


print(dict.keys())
print(dict.values())


# In[93]:


dict.clear()
print (dict)


# ## 9. Defining a Function

# def functionname( parameters ):
#    "function_docstring"
#    function_suite
#    return [expression]

# In[74]:


dict = {'name': 'Zara', 'age': 7, 'class': 'First', 'school': 'DPS School'}
print (dict)
print (dict['name'])


# In[90]:


def printinfo( d ):
    print("name: ", d['name'])
    print("class: ", d['class'])
    print("school: ", d['school'])
    print("age: ", d['age'])
    return;
y=['name: ', 'class: ', 'school: ', 'age: ']
def printinfo2( d ):
    z=0
    for x in list(d.keys()):
        print(y[z], d[x])
        z=z+1
        print (z)
        return z
    return
#printinfo(dict)
printinfo2(dict)


# In[115]:


printinfo(dict)


# In[116]:


def sum( a, b ):
   # Add both the parameters and return them."
   total = a + b
   print ("sum : ", total)
   return total;


# In[118]:


print (sum(4,6))


# ## 10. Exception
# An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. In general, when a Python script encounters a situation that it cannot cope with, it raises an exception. An exception is a Python object that represents an error.
# 
# When a Python script raises an exception, it must either handle the exception immediately otherwise it terminates and quits.

# ### Handling an exception
# If you have some suspicious code that may raise an exception, you can defend your program by placing the suspicious code in a try: block. After the try: block, include an except: statement, followed by a block of code which handles the problem as elegantly as possible.
# 
# ### Syntax

# try:
#    You do your operations here;
#    ......................
# except ExceptionI:
#    If there is ExceptionI, then execute this block.
# except ExceptionII:
#    If there is ExceptionII, then execute this block.
#    ......................
# else:
#    If there is no exception then execute this block. 

# In[119]:


try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")
   fh.close()


# In[121]:


try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")


# ## 11. Classes
# Python has been an object-oriented language since it existed. Because of this, creating and using classes and objects are downright easy. 

# In[91]:


class Employee:
    empCount = 0
    def __init__(self, n, s):
        self.name = n
        self.salary = s
        Employee.empCount += 1
        print("here")
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print ("Name : ", self.name,  ", Salary: ", self.salary)


# In[94]:


emp1 = Employee("Zara", 2000)
emp1.empCount
emp2 = Employee("Manni", 5000)
emp1.empCount


# In[95]:


emp1.displayCount()
emp2.displayEmployee()

