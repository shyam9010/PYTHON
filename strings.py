#"strings are collection  of letters "
#'string has so many methods'

''' replace
upper()
lower()
endswith()
startswith()
lenght()
strip()
lstrip()
rstrip()
count()
remove suffix()
remove prefix()
index()
split
'''

A= "Good Morning"
print(A.lower())
print(A.upper())
print(A.endswith("Morning"))
print(A.startswith("Good"))
print(A.replace("Good","Bad"))
print(A.find("Bad")) # if string is not there it will pass -1 , if there gives 0
print(A.index("Good")) # if string is not there it will throw error, if there gives 0
print(A.count("o")) # gives the count of letter in var
print(A.removeprefix("Good"))
print(A.removesuffix("Morning"))
print(A.split()) #converts string to a list 


B = "   very   Good    "
print(len(A))
print(B.strip())
print(B.lstrip())
print(B.rstrip())