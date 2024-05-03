a = [1, 2, 3, 4, 5]
stack = []
bucket_list = []
for i in a:
    stack.append(i)
while len(stack) > 0:
    bucket_list.append(stack[-1])
    stack.pop()
print(bucket_list)
