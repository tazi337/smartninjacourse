# print welcome to user
print("Welcome")

# read user input for operation
operation = input("Please enter a mathematical sign: ")
print(f"You entered {operation}")

# read user input for first value
val1 = float(input("Please enter a number: "))

# read user input for second value
val2 = float(input("Please enter a number: "))


# calculate depending on operators
# and print result
result = None #None wird hier gesetzt, damit es auf jeden Fall ein Result gibt, dass er unten einsetzen kann.
if operation == "+":
    result = val1 + val2
elif operation == "-":
    result = val1 - val2
elif operation == "/":
    result = val1 / val2
elif operation == "*":
    result = val1 * val2
else:
    print("try again")

print(f"Your result is {result}")




