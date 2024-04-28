# Given two lists .Find and print the elements that are in list1 but not l2.

a = [1, 2, 3, 4]
b = [2, 4, 5, 7]
for i in a:
    for j in b:
        if i != j:
            print(i)
