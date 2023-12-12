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
