# Type Conversion (Automatic)

# Type conversion happens automatically by Python when it converts one data type into another without you writing any code.
a = 10      # int
b = 2.5     # float

c = a + b   # Python converts int to float automatically
print(c)   # Output: 12.5

# Type Casting (Manual)

# Type casting is when you manually change one data type to another using functions like:
# int()
# float()
#  str()

x = "10"        # string
y = int(x)     # manually converting string to int

print(y + 5)   # Output: 15
# Here, you are telling Python to convert "10" (string) into 10 (int).