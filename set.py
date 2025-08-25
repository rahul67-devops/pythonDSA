# DAY 17

"""
1> If we want to represent a group of unique values as a single entity then
we should go for the set.
2>Duplicates are not allowed
3> Insertion order is not perserved.But we can sort the element
4>Indexing or slicing are not allowed .
5> Hetrogenous items are allowed
6>Set objects are mutable i.e once we creates a set objects
we can perform any changes in that object based on our requirements
7> Use curly braces with comma seprator {}
8>Its uses for Apply mathematical operations like union,
intersection, etc on set objects 

Note:-->
s = {} ---> Its consider as a dictionary

"""

# Topic Creation of set

# data = {10,20,30,40}
# print(data) #{40, 10, 20, 30}
# print(type(data)) #<class 'set'>

# We can create set objects by using set function
"""
syntax : s = set(any sequence)
"""

# eg 1
# list_data = [10,20,30,40]
# s = set(list_data)
# print(s) #{40, 10, 20, 30}

# eg2
# s = set(range(5))
# print(s) #{0, 1, 2, 3, 4}

# Note :- While creating empty set whave take special care

# s = {}
# print(s)
# print(type(s)) #<class 'dict'>

# ----
# s = set()
# print(s)
# print(type(s)) #<class 'set'>

# Topic Important functions in set

# 1> add(x):-- Add item x to set

# s = {10,20,30}
# s.add(50)
# print(s) #{10, 20, 50, 30}

# 2.Update(x,y,z)
"""
To add multiple items of argumnets are not individual elements and these
are iterable objects like list, ranges .. All elements present in given 
iterable objects will be added to the set
"""

# s = {10,20,30}
# s.update([70,80,90],"Akash", range(5))
# print(s) #{0, 1, 'A', 2, 3, 4, 70, 'k', 10, 80, 20, 'h', 's', 90, 'a', 30}

# Q Which of Valid set or not?
# s = {10,20,30}
# s.add(10) #Valid
# s.add(40,50,60) #invalid (set.add() takes exactly one argument)
# s.update(55) invalid  #'int' object is not iterable
# s.update([88,77], range(10)) #valid
# s.add([55,77]) #invalid (unhashable type: 'list')
# print(s)

# 3 copy():- Return copy of the set. It is cloned object
# s = {10,20,30}
# s1 = s.copy()
# print(s1) #{10, 20, 30}

# 4> pop() It removes and returns same random element from the set
# s = {40,10,20,30}
# print(s) #{40, 10, 20, 30}
# print(s.pop()) #40
# print(s) #{10, 20, 30}

# 5> remove(x):- Removed specefied  element from the set
# s = {40,10,20,30}
# s.remove(30)
# print(s) # {40, 10, 20}

# 6> discard(x):--It removes specified element form set
# If the specefied element not present in the set then we
# won't get any error

# s = {10,20,30}
# s.discard(10)
# print(s) #{20, 30}
# s.discard(50) #{20, 30}
# print(s)


# 7> clear():-- TO remove all the elements from the set

# s = {10,20,30}
# print(s) #{10, 20, 30}
# s.clear()
# print(s) #set()

# Topic Mathematical operation in set

# 1> Union():--
"""
x.union(y) => It returns all elements present in both sets (If there is 
duplicate values will consider as only one)

syntax:--
x.union(y)  or x|y
"""

# x = {10,20,30,40}
# y = {30,40,50,60}
# print(x.union(y)) #{40, 10, 50, 20, 60, 30}
# print(x|y) #{40, 10, 50, 20, 60, 30}

# 2 Intersection():-> Returns common elements present in x&y
"""
syntax:--
x.intersection(y) or x&y
"""
# x = {10,20,30,40}
# y = {30,40,50,60}
# print(x.intersection(y)) #{40, 30}
# print(x&y) #{40, 30}

# 3. diffrence():- It returns the elements present in x but not in y
# x = {10,20,30,40}
# y = {30,40,50,60}

# print(x.difference(y)) #{10, 20}
# print(y.difference(x)) #{50, 60}

# print(x-y)
# print(y-x)


# Topic Membership operator in set (In, not in)

# s = set("Akash")
# print(s)
# print("d" in s) #False
# print("k" in s) #True


# Topic Set Comprehension

# s = {x for x in range(10)}
# print(s) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(type(s)) #<class 'set'>

# Q Double every element from range 2 to 20
# s = {2*x for x in range(2,21)}
# print(s) #{4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40}

# Q Sqaure the each element from range(5)

# s = {x*x for x in range(5)}
# print(s) #{0, 1, 4, 9, 16}

# Q Wap to eleminate the duplicate present in the list

# list_data = eval(input("Enter the values in the list"))
# s = set(list_data)
# print(s) #{10, 20, 90, 60, 30}
# l1 = []
# for x in list_data:
#     if x not in l1:
#         l1.append(x)
# print(l1) #[10, 20, 30, 60, 90]

