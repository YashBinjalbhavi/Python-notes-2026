# escape sequence character

str1 = "this is a string.\n we are creating it in python"
print(str1)
# \n = means writing the sentence in the next line

str2 = "this is a string.\t we are creating it in python"
print(str2)
# \t = means tab space


# basic string operations
# concatenation means adding two strings

str3 = "yash"
str4 = "bhave"
print(str3 + str4)

# this is how you can find out the length of a string
print(len(str3))

# indexing in python
ind = str3[2]
print(ind)


str5 = "yashbinjalbhavi"
print(str5[:4])     # from starting to fourth index
print(str5[0:])     # from starting till last index
# ending index is always excluded
# negative indexing starts from -1, -2, -3 from the end

str6 = "apple"
print(str6[-3:-1])  # pl


str7 = "hello my name is yash sadanand binjalbhavi"
print(str7.endswith("avi"))   # True
print(str7.endswith("kno"))   # False

print(str7.capitalize())      # capitalize first character
print(str7.replace("yash", "sujal"))
print(str7.find("yash"))
print(str7.count("n"))


name = input("enter your first name : ")
print("the length of your name is :", len(name))


str8 = "hi i $am the $ symbol"
print(str8.count("$"))


marks = int(input("please enter your marks : "))

if marks >= 90:
    grade = "A"
elif marks >= 80 and marks < 90:
    grade = "B"
elif marks >= 70 and marks < 80:
    grade = "C"
else:
    grade = "D"

print("grade of the student ->", grade)


age = int(input("please enter your age : "))

if age >= 18:
    if age >= 80:
        print("you cannot drive")
    else:
        print("you can drive")
else:
    print("you cannot drive")
