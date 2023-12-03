# tuple is ddefined as ()
# it is immutable cannot make any changes
# allow duplicates
# different type of elements
# cant use any methods
# Tuple operations
# Concatenation
# Iteration


t = (1,3,67)

print (type(t))

print(min(t))

print(max(t))

print(t*4) # repetation 

t1 = (3,6,7,8)

print( t+t1) # concatenation

for i in t: # iteration
    print (i)

print(1 in t)

print(2 not in t)  # membership opeartors and identity operators

print (t in t1)

print(t is not t1)