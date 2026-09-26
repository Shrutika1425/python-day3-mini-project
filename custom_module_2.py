# main.py
import custom_module_1 as mymodule

# greet function call
mymodule.greet()

# calculator function call
print(mymodule.calculator(10, 5, "+"))
print(mymodule.calculator(10, 5, "-"))
print(mymodule.calculator(10, 5, "*"))
print(mymodule.calculator(10, 5, "/"))
print(mymodule.calculator(10, 5, "%"))

# variables from module
print(mymodule.username)
print(mymodule.password)