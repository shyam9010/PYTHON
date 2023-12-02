# list is mutable it means we can modify the list
# we can store all  types of elements in list
# allows duplicates
#  allows indexing , both forward and backward

l = []

list = [1,2,3,4,'shyam']

print(list)

print(list[-1]) # it gives the last thing of the list

print (list[2]) # it gives 3 

print(list[0:5:2]) # slicing 

print(list[0:-1])

print (list.append(5)) # add the element in list at last

print(list)

list.extend([3,35,2,7,8]) # to add bulk data to the list 

print(list)

print(list.count(3)) # gives count of element in list

list.remove(3) # remove the element directly

print(list)

list.pop(4) # it remove the element by using index of the list

print(list)

print(list.index(2)) # gives the index of the value

list.insert(1,'sundar') # to insert the element in a particular location ion the list

print(list)

for i in [1,2,3,4,'shyam']:
    print(i)
 