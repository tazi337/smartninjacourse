# Write a loop, which asks for an input,
# until you entered a valid operator

# hint:
# "+" in "+-/*"
# "+" in ["*", "+", "-", "/"]

operator = None
while operator not in ("+", "-", "*", "/"):
    operator = input("Please input a valid operator")
else:
    print("Thanks!")




print("+-" in "+-/*")                # True
print("+-" in ["*", "+", "-", "/"])  # False

