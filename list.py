"""
LIST array in c/c++/java (collections) (Group of elements in a single entity)
If we want to represent a group of individual objects as a single
Entity where insertion order is preserved and duplicates are allowed
then we should go for list.
Note:-1> In List the elements will be placed within square brackets and 
         the comma seprator.
      2> List is Mutable, SO we can change the contents.
      3> Index will play very important role and Python supports
      +ve and and -ve index. Positive means from left to right 
      and Negative means right to left.
      4> We can store any kind of data in the list (Hetrogenous data)
"""
# Topic Creation of List Object

# 1 We can create an empty list object

# list = []
# print(list)

# 2 If we know elements already then we can create list as follows
# list = [10,20,30,40]

# 3> List with Dynamic Input:- 
# list = eval(input("Enter a list"))
# print(list)
# print("Type of ",type(list))

# 4> With list() function

# 1> data = list("Aakash")
# print(data)# ['A', 'a', 'k', 'a', 's', 'h']

# 2>
# data = list(range(5,11))
# print(data) # [5, 6, 7, 8, 9, 10]

# 5 Split function

# data = "Welcome to the Programming World"
# out_data = data.split()
# print("output: ", out_data)

# Topic:  Accessing elements of List
"""
There are Two Ways
1> Index 
2> Slice operator
"""

# 1 By Using Index:--->

# data = [10,20,30,40]
# data[0] # 10
# data[2] #30
# data[-1] # 40

# 2 By using Slice Operator
"""
[begin:stop:step]
or
[start:stop:step]
"""

# data = [0,1,2,3,4,5,6,7,8,9,10]
# print(data[2:7]) # [2, 3, 4, 5, 6]
# print(data[::-1]) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#  Topic : :List vs Mutability
"""
Once we creates a list objects.We can modify its content.
Hence list of objects are Mutable

Note: Mutable object Supports item assignment 
"""

# data = [0,1,2,3,4,5,6,7,8,9,10]
# data[3] = 777
# print(data) # [0, 1, 2, 777, 4, 5, 6, 7, 8, 9, 10]

# data[7] = "Manish"
# print(data)

# Topic : Traversing the elements of List
"""
The sequential access of each element in the list
is called traversal. 
"""

# 1> By Using While Loop

# data = [10,20,30,40,50] 

# i = 0
# while i<len(data):
#     print(data[i])
#     i = i + 1

# 2> By using for Loop

# data = [10,20,30,40,50] 

# for element in data:
#     print(element)

# Q WAP to print only Even No 
# data = [0,1,2,3,4,5,6,7,8,9,10]

# data = [0,1,2,3,4,5,6,7,8,9,10]
# for ele in data:
#     if ele % 2 == 0:
#         print(ele)

# Q To Display an elements by index wise i.e +ve and -ve

# data = ["A","B","C","D"]
# len = len(data)
# i = 0
# for i in range(len):
#     print('{} is available at +ve index:{} and -ve index:{}'.format(data[i], i, i-len))

#  i-len
# 0-4 ---> -4

"""
A is available at +ve index:0 and -ve index:-4
B is available at +ve index:1 and -ve index:-3
C is available at +ve index:2 and -ve index:-2
D is available at +ve index:3 and -ve index:-1
"""

# Topic:-- Important function of LIST

# 1> len():-> Return No of elements present in the list

# data = [10,20,30,40,50] 
# print(len(data))

# 2> count():-> It returns No of occurences of specified item in the list

# data = [1,2,2,2,1,3,4,3,3] 
# print(data.count(4)) #1
# print(data.count(2)) #3

# 3> Index() function :-> It returns the index of first occurence of the specified item
# data = [1,2,2,2,1,3,4,3,3]
# print(data.index(3)) #5

# print(9 in data) # False (if element is not peresent in the list so will get the value error)

# Q WAP to use count or membership operator to check whether the element present in list
# or not
# data = [1,2,2,2,1,3,4,3,3] 
# take_input = int(input("Enter the value to find index"))

# if data.count(take_input):
#     print(take_input, "at availabe in this index", data.index(take_input))
# else:
#     print(take_input, "is not available")


# Day 15
# Topic Manipulating list Element

# 1 Append Function():--> We can use append() function to 
# add item at add the end of the list.

# data = []
# data.append("Akash")
# data.append("Practice")
# data.append("Kiya")
# print(data)

# Q Wap to add all the elements to list upto 100
#  which is divisible by 10

# lst = []

# for i in range(1,101):
#     if i % 10 == 0:
#         lst.append(i)
# print(lst)


# 2>  Insert function():-  To insert an item at specified index positon

# data = [1,2,3,4]
# data.insert(1, 888)
# print(data) [1, 888, 2, 3, 4]

"""
Note:-
If the specified index is greator than max index then element
will be inserted at last  position. if the specified index is 
smaller that min index then the element be will inserted at 
the first postion
"""

# data = [1,2,3,4,5]
# data.insert(50,777)
# print(data) #[1, 2, 3, 4, 5, 777]
# data.insert(-12,222)
# print(data) #[222, 1, 2, 3, 4, 5, 777]

# H.W Diff betwn append() and insert() function (IQ)

# 3 extend() function:--> To add all items of one list to another list

# veg_items = ["Paneer", "Mix-Veg", "Dal-Tadka"]
# nonVeg_items = ["Biryani", "Chicken Tandoori", "Shorma"]

# veg_items.extend(nonVeg_items)
# print(veg_items) # ['Paneer', 'Mix-Veg', 'Dal-Tadka', 'Biryani', 'Chicken Tandoori', 'Shorma']

# 4 remove() function
"""
To remove the specified item form the list.If the item present
multiple times then only first occurrence will be removed.
"""

# data = [10,20,10,30]
# data.remove(10)
# print(data) #[20, 10, 30]

"""
Note:- If the specified element not present in the list
      so will get the value error.
"""

# data = [10,20,10,30]
# data.remove(50)
# print(data) # ValueError: list.remove(x): x not in list

# 5 pop() function:-
"""
It removes and returns the last element of the list.
This is the only function which is manipulates list and 
returns some element.
"""

# data = [10,20,30,40]
# print(data.pop()) # 40
# print(data) #[10, 20, 30]

"""
Note:->
If the list is empty then pop() function raises the index error
"""
# list_data = []
# print(list_data.pop()) #IndexError: pop from empty list

# Q How to remove the specified index element
# data = [10,20,30,40]
# print(data.pop(2)) #30
# print(data) #[10, 20, 40]


# List in Dynamic/Growable:-->
"""
append(), insert(), extend()--->Increasing
remove(), pop() ---> To decrease the size
"""

# Topic:-- Ordering Elements of List

# 1> reverse():- IT use to reverse the order of the element of the list

# data = [10,20,30,40]
# data.reverse()
# print(data) #[40, 30, 20, 10]

# 2> sort()
"""
Default orders
1> for numbers:-- Ascendig order
2> for string :-- Alphabetical Order
"""

# data = [10,5,0,20,15]
# data.sort()
# print(data) #[0, 5, 10, 15, 20]

# data = ["dog", "cat", "tiger", "zebra", "lion"]
# data.sort()
# print(data) #['cat', 'dog', 'lion', 'tiger', 'zebra']

"""
sort accourding to reverse of default natural sorting 
order by using reverse = True argument
"""

# data = [40,10,30,20]
# data.sort()
# print(data) #[10, 20, 30, 40]

# data.sort(reverse=True)
# print(data) #[40, 30, 20, 10]
# data.sort(reverse=False)
# print(data) #[10, 20, 30, 40] 

# data = ["Mukul","Ankit","Jackson", 20, 40]
# data.sort(reverse=True)
# print(data) #['Mukul', 'Jackson', 'Ankit']

"""
Note:- 
IF we use diffrent or mix data type in the list and when we apply 
the sort() function then will get TypeError
"""

# Topic:--->  Aliasing and cloning of List objects (IQ)
# Aliasing --> Shallow Copy
# cloning --> Deep copy

"""
The process of giving another reference variable to the existing 
list is called aliasing (Shallow Copy)
"""

# x = [10,20,30,40]
# y = x
# print(id(x)) #2547395744384
# print(id(y)) #2547395744384

"""
Note:--
The problem in this approach is using one reference variable if we
are changing the content then those changes will reflected to the 
other reference variable
"""

# x = [10,20,30,40]
# y = x
# y[1] = 777
# print(x) #[10, 777, 30, 40]
# print(id(x))
# print(id(y))

"""
Note:- 
To overcome this problem we should go for cloning (Deep copy).
The process of creating exacalty duplicate(replica) independent
object is called Deep copy(cloning)

We can implement Deep copy by using slice operator or
by using "copy()" function
"""

# 1> By using slice operator

# x = [10,20,30,40]
# y = x[:]
# y[1] = 77
# print(x)
# print(id(x)) #1781725221504
# print(id(y)) #1781727393472

# 2> By using copy() function

# x = [10,20,30,40,50,60]
# y = x.copy()
# y[1] = 888
# print(x) #[10, 20, 30, 40, 50, 60]
# print(y) #[10, 888, 30, 40, 50, 60]

#  day 16 Topic Using Matheatical operations in the list objects

# 1 concatination operator(+)

# data1 = [10,20,30]
# data2 = [40,50,60]

# ans_data = data1 + data2
# print(ans_data) #[10, 20, 30, 40, 50, 60]

"""
Note:- To use + operator compulsary both arguments should be list objects,
      otherwise will get type error.
"""

# ans_data = data1+40
# print(ans_data) #TypeError invalid case
# ans_data = data1+[90]
# print(ans_data) #[10, 20, 30, 90] valid case

# 2 Repetation Operator(*)
"""
* opertor to repeat elements of list specified no of times
"""
# data1 = [10,20,30]
# out_data = data1*3
# print(out_data) #[10, 20, 30, 10, 20, 30, 10, 20, 30]

# Topic Comparing List objects

# x = ["Dog", "Cat", "Rat"]
# y = ["Dog", "Cat", "Rat"]
# z = ["DOG", "CAT", "RAT"]

"""
Note:--
1> The no of elements should be same 
2> oreder of elements
3>The content of elements (case sensative)
"""

# print(x==y) #True
# print(x==z) #False
# print(x!=z) # True

# print(ord("A")) #65
# print(ord("a")) #97

"""
Note:-- 
Whenever we are using relational operator (<,<=,>,>=)
between list objects only first element comparison performed
"""

# x = [10,20,30,40,50]
# y = [70]

# print(x<y) #True

# Topic Membership operator

"""
We can check whether element is a member of the list
or not by using membeship operator


syntax:-->
[in operator]
[not in operator]
"""

#  Topic clear() function

"""
We can use clear() function to 
remove all the elements of the list
"""

# data = [10,20,30,40]
# print(data) #[10, 20, 30, 40]
# data.clear()
# print(data) # []


#  Topic Nested List
"""
Sometimes we can take one list inside
anothe list such type of list is called nested list.
"""

# ex Nested list as a matrix

data = [[10,20,30], [40,50,60],[70,80,90]]
# print(data)
# for x in data:
#     print(x)

"""
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]
"""

# print("Elements by Matrix Style")

# for i in range(len(data)):
#     for j in range(len(data[i])):
#         print(data[i][j], end="")
#         print()


#  Topic Delete element using del keyword

# data = [10,20,30,40]
# print(data)
# del data[2]
# print(data)

#  Topic List Comprehension (IQ) imp

"""
Creating a list objects from any iterabl
objects like (list,tuple,dict,range,etc)
based on some condition

synatx:-->
      
      list[expression for item in list 
                  if conditon]
"""

# without using list comprehension

# data_list = []
# for x in range(1,11):
#     data_list.append(x)

# print(data_list) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension

# data_list = [x for x in range(1,11)]
# print(data_list) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Q WAP to perform the square using List comprehension
# data_list = [x*x for x in range(1,11)]
# print(data_list) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# # WAP to perform the square of even for 1 to 10 using List comprehension
# data_list = [x*x for x in range(1,11) if x%2==0]
# print(data_list) # [4, 16, 36, 64, 100]

# # WAP to double values form 1to100 where no should divisible by 3

# data_list = [2*x for x in range(1,101) if x%3==0]
# print(data_list)

# Q Wap to select the No's that present in N1 but not in N2

# N1 = [10,20,30,40]
# N2 = [30,40,50,60]

# out_list = [x for x in N1 if x not in N2]
# print(out_list) #[10, 20]

# Q WAP to convert string into the Uppercase using list comprehension

# words = "welcome to the jungle"
# words_into_list = words.split()
# # print(words_into_list)
# list_out = [w.upper() for w in words_into_list]
# print(" ".join(list_out))


