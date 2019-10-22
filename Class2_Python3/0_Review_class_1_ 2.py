# questions from last lesson #
x="b"
x="a"

# QUESTION 1 #
# space after function name is allowed
# (as many as u like)

print (1)
print(1)

# space as first element of the line
# is an error
print(1)

# except if it's a part of a clause
if True:
 print(1)

var1_=1
x="a"

# QUESTION 2 #
# difference between "==" and "is"
# "==" equality operator - checks if values are equal
# "is" identity operator - checks whether identity is equal
print("x"*20)
x = 1   # int
y = 1.0 # float
print(y == x)   # True
print(y is x)   # False
print(type(y) is float) #True

# for now just use "=="
# it helps avoid errors
# we rarely use the "is" operator
#
# today we will investigate a
# further possible usage of the is operator

