# dict is defined in {a:"shyam"}
# key is immutable
# key acts as index
# value can be anything 
# no slicing 
# keys are unique (no duplicates)


# methods 
# get()
# update()
# values()
# keys()
# items()

d = {1:'abc',22:'shyam','python':2}

print(d[1])

# get()

print(d.get(22))

#keys

print(d.keys())

#values

print(d.values())

#items

print(d.items())

for i in d:
    print(d)

#update

print(d.update({11:234}))

print(d)


# to get dict values in iteration we us items and declare two var

for i,j in {1:'abc',22:'shyam','python':2}.items():
    print(i,j)