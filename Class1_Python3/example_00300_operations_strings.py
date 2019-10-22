greeting = "Hello World!"
name = "Smartninja!"

# ADDING STRINGS (CONCAT)
print(greeting)
print(greeting + " - AI ")

# MULTIPLYING STRINGS - das Beispiel hier erzeugt einen String mit 20 Sternchen
print("*" * 20)

# PRINTING THEM BY INSERTING
print("Greeting: {}, Name: {}".format(greeting, name))
# new in Python 3:
print(f"Greeting: {greeting}, Name: {name}")
# durch "f" wird es ein formatierbarer String, ich kann Variablen hinzufügen in geschwungener Klammer

# CHECKING FOR (UN)EQUALITY
print(greeting == name)
print(greeting == "Hello World!")

# CHECKING FOR OCCURRENCE
print(greeting in "Hello World! is the first greeting in a computer language")
# checken, ob etwas bestimmtes in einem text vorkommt.
# genauer definieren könnte man es noch mit regex (folgt später)

# WATCH OUT FOR USING THE CORRECT TYPES
print("3" + "3")
print(int("3") + int("3"))
print(str(3))

# print int("3") + "3"      # TypeError
# print int("a")            # ValueError
