a_list = []
b_list = [1, 2, 3, 4]
print(a_list)
print(b_list)

# reference
# print a_list[0]  # IndexError, because has no elements
print(b_list[1])  # 2
b_list[1] = 10
print(b_list)

# slice
print(b_list[1:3])  # [10, 3] #Erster Index ist einschließlich - ist dabei, Schlussindex ist ausschließlich - nicht mehr dabei
print(b_list[1:-1])  # [10, 3]
print(b_list[-2:])  # [3, 4] #am schluss nichts, heißt, bis zum Ende (alles inkludiert)
print(b_list[::-1])  # [4, 3, 10, 1] #Doppel-Doppelpunkt zeigt an, wie ich durch die Indizes durchgehe
print(b_list[::-2])  # [4, 10]
# [start : end : iterationrule]
# iterationrule < 0 : reverse
# iterationrule = 2 : every other
