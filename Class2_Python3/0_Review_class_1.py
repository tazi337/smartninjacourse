# we learned how to make comments

# we learned how to use output
# and other types on the terminal

print("Hello World!", "I am your computer")

# we learned how to set variables
# and operate on them

x = 25
y = 2
z = x / y

print("z = ", z)

# we learned that there are many different
# types of values available in Python

a = 1  # int
b = 1.0  # float
c = "1"  # string
T = True  # Bool
F = False  # Bool

# you can alternate between types
# and check them

d = int(c)
e = d + a
print("the variable e is of type:", type(e), "and has the value:", e)

# we learned about different comparative operators

x = 1
y = 2

print(x == y)  # False
print(x < y)  # True

# we learned how to input values
# while the code is running

x = input("please input a value for x:")

# we learned about conditions
# and the usage of indentations in the code


if x == 2:
    print("x equals 2")
elif x == 1:
    print("x equals 1")
else:
    print("x doesnt equal 1 or 2")

x = True
print(x)
