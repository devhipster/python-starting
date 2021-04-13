#comprehensions = python lists ,sets and dictionaries


""" List comprehensions """
# A list  comprehension is basically a one line for loo that produces a python list data strcutreself.

x = [c for c in range(3)]
b = list(range(0,3))
print(b)

#create a filter with list comprehensions 
x = ['1', '2','3','4','5']
y = [int(i) for i in x]
print(y)

vec = [ [1,2,3], [4,5,6],[7,8,9] ]
all = [num for elem in vec for num in elem]
print(all)

"""Dictionary comprehensions"""
