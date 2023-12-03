#set is defined as {}
# do not allow duplicates
# no INdex
# unordered  , will print randomly 
# donot allow mutable types of set elements


s = {1,2,3,4,5}

# add

s.add(9)

print(s)

#update

s.update({1,4,77,88})

print(s)

#pop

s.pop()

print(s)

#remove

s.remove(4)

print(s)

#union

s1 = {33,1,3,5,6}

print(s.union(s1) )

#intersection

print(s.intersection(s1))

#subset

print(s.issubset(s1)) # the elements in s shoul;d be there in s1

print(s.issuperset(s1)) # elements in s should be there in s1 

print(s.isdisjoint(s1))

print(s.difference(s1))