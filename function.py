# Day 19

"""
Functions

In python supports 2 types of function
1> Built in Function
2> User Defined Function


1> Built in Function:--> Predefined python functions is nothing 
but the  Built in Function.
eg --> print(), len(), id(), input(), type()..etc

2>User Defined Function:->Devloped by programmer to perform
some tasks are called user defined function.

DRY--> Dont Repeat Yourself

syntax:-- To create User Defined Function

def functin_name(parameters):
    '''doc string'''
    ----------------
    ----------------
    return Value

Note:-- While creating a functions we can use 2 keywords
1. def (Mandtory)
2. return (optional)
3. We cant use exisiting function name to create user defined function
4.pareters(optional)
5.The function should not define with the numbers or the special characters
except underscore(_).
"""

#  Wap to to wish Good morning

# def wish_me():
#     print("Good Morning")


# wish_me()# calling this function as many time that we want
# wish_me()
# wish_me()

# Topic Parameters 
"""
1.Parameters are inputs to the function.
2.If a function contains parameters, then at the time of calling
compulsary we should provide the values otherwise 
we will get error.
"""

# Q Write a function to take name of the student as an input
# and print with message by name

# def wish_me(name):
#     print("Hello", name, "Good Morning")

# wish_me("Akash")
# wish_me("Atul")
# wish_me("Mia")
# wish_me("John")

"""
Hello Akash Good Morning
Hello Atul Good Morning
Hello Mia Good Morning
Hello John Good Morning
"""

# method2
# name = input("Enter the Name of the student: ")
# def wish_me(name):
#     print("Hello", name, "Good Morning")

# wish_me(name)

# Wap to create function square of no and no is taking from keyboard

# def squareIt(num):
#     out = num*num
#     print("Square of a number ", out)

# num = int(input("Enter a no: "))
# squareIt(num) #Square of a number 49

# Topic Return Statement

"""
1.Function can take input values as a parameter
and execute business logic and returns output to the
caller with return statement.
2.We can return not only the parameters but also we 
can return the defined variables and the datasets.
Note:--> If we are not writing return statement
then default return value is None.

"""

# def squareIt(num):
#     return num*num

# number = int(input("Enter the number: "))
# First way of calling via object
# obj = squareIt(number)
#second way of calling via Print satatement
# print("The square is: " ,obj)
# print("The square of Number: ", squareIt(number))


# wap to create function of additon of 2 no's and no is taking from keyboard

# def addition (num1, num2):
#     return num1 + num2

# num1 = int(input('enter a num1 : '))
# num2 = int(input('enter a num2 : '))

# print("addtion of 2 no", addition(num1,num2)) 

# Day 20

# Q Write a function to check whether no is even or add i/p from keyboard.

# def check(num):
#     if num % 2 == 0:
#         print('Number is even', num)
#     else:
#         print('number id odd', num)

# user = int(input("Enter a number: "))
# check(user)

#  WAP to create a function to check the no is positive or negative.

# def check (num):
#     if num > 0:
#         print('Number is positive', num)
#     else:
#         print ('number is Negetive', num)

# user = int(input("Enter a number: "))
# check(user)

# WAP to create a function if string length is greator than 5 then print(GOOD String)
# else print (BAD String) and string taking I/P from keyboard.

# def check_string(s):
#     if len(s) > 5:
#         print("Good String")
#     else:
#         print("Bad String")
# user_input = input("Enter a string: ")
# check_string(user_input)

# WAP to create a function to check simple interest P*N*R/100  
# WAP to  create a function to reverse a string

# def name(str):
#     return str[::-1]

# user = input("enter a string: ")
# a = name(user)
# print(a)

# str(input(""))
# WAP to  create a function to check palindrome

# "MOM" = "MOM"
# ""

# day 22
# Topic Returning Multiple Values from a functions.

"""
In other Language like c,c++ and Java function
Can almost return  one value but in python a function can return
any number of values.
"""

# def sus_sub(a,b):
#     sum = a+b
#     sub = a-b
#     return sum, sub

# x,y = sus_sub(40,20)
# print("The Sum", x)
# print("The Sub", y)

# """
# The Sum 60
# The Sub 20
# """

#  WAP to create a calculator function using multiple return 

# 1> Topic Default Arguments
"""
Sometimes we can provide default for our
postional arguments
"""

# def wish(name="Akash"):
#     print(f"Hello, {name}, Good Morning")

# wish() #Hello, Akash, Good Morning

"""
Note:--> If we are declaring defalut arguments then these should
be a last argument
eg--> def wish(a,v,name="Akash")
"""

# 2> Topic:--> Postional Argumrnts
"""
Arguments passed to function in correct 
positional order.
"""

# def sub(a,b):
#     print(a-b)

# sub(90,60)
# sub(80,10)
"""
Note:-->
The Number of arguments and postion of arguments must be 
matched. If we change the oreder then result may be changed.
The order of arguments and positon of argument both are important.
"""

# 3> Topic Key-word Arguments:-
"""
We can pass arguments values by keyword 
i.e by parameter name.
"""

# def sub(a,b):
#     print(a-b)

# # 1st way of call
# sub(a=100, b=200)# order is not required
# sub(b=200, a=300)
# # 2nd way of call Taking i/p from keyboard
# x= int(input("Enter 1st no: "))
# y= int(input("Enter 1st no: "))
# T = sub(x,y)
# print(T)

"""
Note:--> Always pass first Positional Arguments then after key-word argument
"""

# 4> Variable Length arguments:
"""
Sometimes we can pass variable number of arguments to our function,
such type of arguments are called variable lenght arguments.

Symbol is * as follows

syntax:-- def f1 (*n)
"""
# def add(*n):
#     total = 0
#     for n1 in n:
#         total = total + n1
#     print("The sum= ", total)

# add()
# add(10,20)
# add(10,20,30)

"""
The sum=  0
The sum=  30
The sum=  60
"""

"""
Note:-> We can mix Variable length argument with positional 
argument
"""
# def f1(x, *n):
#     print("Normal Argument--> ", x)
#     print("Variable-Length Argument--> ")

#     for n1 in n:
#         print(n1)

# f1(10,20,30,40)

"""
Normal Argument-->  10
Variable-Length Argument-->
20
30
40
"""

"""
Note:--> After valriable length arguments of we are taking any other
arguments then we should provide as a keyword arguments.
"""

# def f2(*n, x):
#    print("Normal Argument--> ", x)
#    print("Variable-Length Argument--> ")
#    for n1 in n:
#       print(n1)

# f2(10,20,x=30)

"""
Normal Argument-->  30
Variable-Length Argument-->
10
20
"""
# Topic Variable Length Key-word arguments
"""
f1(*n): Variable lenght arguments
f2(**n): Variable Length Key-word arguments
note:- It acts like a Dict
"""
# def f1(**kwargs):
#    print("Variable Length Key-word arguments method")

#    for k,v in kwargs.items():
#       print(f"{k}={v}")
   
# f1(x=10,y=20,z=80)
# f1(name="Ankit", sub="python",
#    gf="Mia")

"""
name=Ankit
sub=python
gf=Mia
"""

# Valid scenario

"""
def f1(x,y,x *n, name="Akash")
ex-> f1(10,20,30, 40,50,60 name="Atul")
"""

# case Study

def f1(arg1, arg2, arg3=4, arg4=8):
    print(arg1,arg2,arg3,arg4)

# f1(3,4) 
# f1(10,20,30,40)
# f1(89,33,arg4=200)#89 33 4 200
# f1(arg4=55,arg3=33,arg2=7) #invalid
# f1() # invalid
# f1(4,6, arg2=7)
# f1(arg3=40, arg4=80,10,30) # invalid
# f1(4,5,arg3=77, arg4=55) #4 5 77 55
