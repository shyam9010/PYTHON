# count the no of K inlist
a = [1, "k", 2, "k"]
count = 0
for i in a:
    if i == "k":
        count = count + 1
print(count)
