no_of_inputs = int(input("enter no of inputs"))
list_a =[]
for i in range(no_of_inputs):
    b=int(input("Enter the inputs"))
    list_a.append(b)
min_num = int(input("min_num = "))
for i in list_a:
    if min_num<i:
        print(i)