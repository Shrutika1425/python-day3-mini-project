# Math function in python
# Python has set of built in math functions including an extensive math module

# 1] Min & Max function
# They are used to find lowest or the highest values
print("--- 1] Min & Max ---")
x = min(45, 33, 12, 67)
y = max(45, 33, 12, 67)

print(x) # Output: 12
print(y) # Output: 67




# 2] Power function
print("\n--- 2] Power function ---")
x = pow(4, 3)
y = pow(7, 2)

print(x) # Output: 64  (4*4*4)
print(y) # Output: 49  (7*7)




# 3] Math module
# Python has also a built in called math which has set of function that can use for mathematical operations
# Math module can be used using import keyword

# i] Square root function
print("\n--- i] Sqrt function ---")
import math
x = math.sqrt(64)
y = math.sqrt(49)

print(x) # Output: 8.0
print(y) # Output: 7.0





# ii] ceil & floor function
print("\n--- ii] ceil & floor ---")
# ceil function rounds of the number to the next nearest integer
# floor function rounds of the number to the previous integer number
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # Output: 2
print(y) # Output: 1





# iii] Pi constant
print("\n--- iii] Pi constant ---")
import math

x = math.pi

print(x) # Output: 3.141592653589793