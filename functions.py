# Day 06 - Functions with Parameters - Easy Version

# 1. Simple function - no parameter
def say_hello():
    print("Hello Shrutika!")

say_hello()




# 2. Function with 1 parameter
def greet(name):
    print(f"Hello {name}!")

greet("Shrutika")
greet("Om")





# 3. Function with 2 parameters
def add(a, b):
    print(a + b)

add(5, 3)  # Output: 8
add(10, 20) # Output: 30






# 4. Function with return
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result) # Output: 20





# 5. Practical Example
def table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

table(3)
print("---")
table(5)