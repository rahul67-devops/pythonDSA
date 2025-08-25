# Tuple Day 16

"""
1. Tuple is exactly same as list except tha is immutable i.e once
we create tuple object, we cannot perform any changes in that object

2. If our data is fixed and never changes then we should go for 
  tuple.
3. Insertion order is preserved
4. Duplicates allowed
5. Multiple object (Hetrogenious) are allowed
6.We can represent Tuple elements within Paranthesis() and
with comma seprator. Parathesis are optional but recommended to use
7.We can preserve insertion order we can diffrentiate duplicates object 
by using index. Hence, index will play very imp role in tuple.

Note:--> We should take special care about single valued Tuple.
Compulsary the value should ends with comma, Otherwise its not 
treated as tuple

"""

# t = (10,20,30)
# print(t)
# print(type(t)) #<class 'tuple'>


# t = (10,)
# print(t)
# print(type(t)) #<class 'tuple'>

#  Topic Accessing Elements of Tuple
# Acces by using index or by slice operator

# 1 By using index:--

# t = (10,20,30,40,50)
# print(t[0]) #10
# print(t[-1]) #50

# 2 By using Slice Operator
# t = (10,20,30,40,50,60,70,80,90)
# print(t[2:5]) #(30, 40, 50)
# print(t[:3]) #(10, 20, 30)

# Topic Tuple vs Immutability
"""
Once we create tuple we can not changes its content.
Hence, tuple objects are immutable.
"""

#  Topic Mathematical Operator in Tuple

# 1> Concatination operator (+):
# t1 = (10, 20, 30, 40)
# t2 = (60,70,80)
# t3 = t1+t2
# print(t3) #(10, 20, 30, 40, 60, 70, 80)

# # 2 Multipication operator (*):
# t1 = (10, 20, 30, 40)
# t2 = t1*3
# print(t2) #10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40)



# Topic Important Function in Tuple

# 1 len():-> To return No of elements in Tuple

# t = (10, 20, 30, 40)
# print(len(t)) #4

# 2 count():-- To return no of occurances of given element in tuple
# t1 = (10, 20, 30, 40,20,20,30)
# print(t1.count(30)) #2

# 3 index():- Retutn index of first occurence of the given element.
# If the specified element is not available then will get the error.

# t = (10, 20, 30, 40)
# print(t.index(20)) #1
# print(t.index(30)) #2
# print(t.index(50)) # ValueError

# 4 sorted():- To sort based on default natural sorting oreder

# t = (30,10,40,20)
# t1 = sorted(t)
# print(t1) #[10, 20, 30, 40]

# 5 Min() and Max Function
"""
These functions return min and max values accourding
to default natural sorting order

"""

# t = (30,10,40,20)
# print(min(t)) #10
# print(max(t)) #40

#  Topic Tuple Packing and Unpacking

#  We can create a tuple by packing a group of variables

# for packing
# a=10
# b=20
# c=30
# t = a,b,c
# print(t) #(10, 20, 30)
# print(type(t)) #<class 'tuple'>

# For unpacking :- Reverse processs of Packing
# t = (10,20,30,40)
# a,b,c,d=t
# print(a,b,c,d) # 10 20 30 40

"""
Note:-- Tuple comprehension not applicable bcs the objects is created 
i.e generator
"""

# HW Diff btween list vs Tuple ----IQ
