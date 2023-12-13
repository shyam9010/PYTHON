class MyClass:
    attribute1 = "Hello"
    attribute2 = 42

    def method1(self):
        return "Method 1 called"

    def method2(self, parameter):
        return f"Method 2 called with parameter: {parameter}"
# Creating an instance of MyClass


obj = MyClass()

# Accessing attributes
print(obj.attribute1)  # Output: Hello

# Calling methods
print(obj.method1())  # Output: Method 1 called
print(obj.method2("World"))  # Output: Method 2 called with parameter: World


class Dog:
    # Class variable
    species = "Canis familiaris"

    # Constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        print(f"{self.name} says Woof!")

    def get_age(self):
        return self.age


# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing attributes
print(f"{dog1.name} is {dog1.get_age()} years old.")
print(f"{dog2.name} is {dog2.get_age()} years old.")

# Calling methods
dog1.bark()
dog2.bark()
