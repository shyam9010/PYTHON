# func is a block of code
# only runs when it is called

def func(a,b,c): # function defination
    print("this is function", a ,b, c)  # function body
func(1,2,3) # function call


def fun(*a): 
    print("this is orbitary function where we can pass no of arg in one parameter",a)
fun(1,2,4,5,7)

def funct(**a):
    print("this is keyword arg will store arg in dict", a)
funct(a=1,b=3)

# nested function 

def outer():
    print("outer function")
    def inner():
        print("inner function")
    inner()
outer()

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
