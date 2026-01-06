# datatype is used to recognize what kind of data variable holds.

# in python, datatype is categorise into 3 parts: numeric, boolean and collection
# in python, there is no limit on data

# in numeric  :int, float and complex
# in booelan  : bool/boolean
# in collection : string,list,tuple,set,frozenset and dictionary

# Numeric data type
#int : whole numbers
#float: decimal numbers
#complex: the number which is written in the form of a+bj 
#         where a and b can be int or float and j is imagenery number
#         j = under root -1


a = 10
b = 10.5
c = 10+12.3j

print(a,type(a))
print(b,type(b))
print(c,type(c))

#boolean : used to store yes-no type value. it has only 2 values True & False

d = True
e = False

print(d,type(d))
print(e,type(e))

# True <class 'bool'>
# False <class 'bool'>

f = 'z'
g = 'python123$'
h = "java@@12"
i = "5646464"

print(f,type(f))   
print(g,type(g))
print(h,type(h))
print(i,type(i))

# z <class 'str'>
# python123$ <class 'str'>
# java@@12 <class 'str'>
# 5646464 <class 'str'>

# we cant write multi line string using single or double quotes in python ex -
# k = "my name is tejas
# i live in thane"

j = """my name is yash
    i live in ambernath"""
      
k = '''my name is yash
    i live in ambernath'''

print(j,type(j))
print(k,type(k))

#list

fruits =["apple","banana","mango"]
print(fruits,type(fruits))
# ['apple', 'banana', 'mango'] <class 'list'>
# list is mutable
# you can change it after its created


#tuple

colors = ("red","green","yellow")
print(colors,type(colors))
# ('red', 'green', 'yellow') <class 'tuple'>
# tuple is immutable
# you cannot change it after its created


#set

number = {1,2,3,4,5}
print(number,type(number))
# {1, 2, 3, 4, 5} <class 'set'>
# A set is like a bag of unique items
# set is mutable

#frozen 

fs = frozenset([1, 2, 3])
print(fs,type(fs))
# frozenset({1, 2, 3}) <class 'frozenset'>
# A frozen set is a locked set
# Same as set but immutable

#dictionary

student = {
    "name": "Yash",
    "age": 21,
    "course": "Python"
}
print(student["name"])
# Yash
# ✔ Keys are unique
# ✔ Values can be anything

# List is mutable → ✅

# Tuple is immutable → ✅

# Set removes duplicates → ✅

# Frozenset is immutable set → ✅

# Dictionary stores key-value pairs → 



# | Type       | Ordered | Changeable | Duplicates |
# | ---------- | ------- | ---------- | ---------- |
# | List       | ✅       | ✅          | ✅          |
# | Tuple      | ✅       | ❌          | ✅          |
# | Set        | ❌       | ✅          | ❌          |
# | Frozen Set | ❌       | ❌          | ❌          |
# | Dictionary | ✅       | ✅          | ❌ (keys)   |

