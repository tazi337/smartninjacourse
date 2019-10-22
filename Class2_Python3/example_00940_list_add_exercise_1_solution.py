# take your shopping list, "bread", "butter", "chocolate"
# you are on a diet, and decide to remove "chocolate"
# print the list before and after removing
meals = ["bread", "butter", "chocolate"]
print(meals)
meals.remove("chocolate")
#meals = meals[:2]
print(meals)

# instead, you will add "proteins"
# append it to your list, and print your list
meals.append("proteins")
print(meals)


# extra: try adding elements to the list by
# 1) adding (+)
# 2) extending
meals += ["cola"]
print(meals)
meals.extend(["cookies"])
print(meals)