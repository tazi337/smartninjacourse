# take your shopping list, "bread", "butter", "chocolate"
# you are on a diet, and decide to remove "chocolate"
# print the list before and after removing

shoppinglist = ["bread", "butter", "chocolate"]
print(shoppinglist)

shoppinglist.remove("chocolate")
print(shoppinglist)

# instead, you will add "proteins"
# append it to your list, and print your list

shoppinglist.append("proteins")
print(shoppinglist)

# extra: try adding elements to the list by
# 1) adding (+)
# 2) extending

shoppinglist += ["fries"]
print(shoppinglist)

shoppinglist.extend(["cheese"])
print(shoppinglist)



