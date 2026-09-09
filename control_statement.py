# Day 04 - Control Statements in Python

# 1. Simple IF statement
age = 18
if age >= 18:
    print("You are an adult")

# 2. IF-ELSE statement
marks = 45
if marks >= 35:
    print("PASS")
else:
    print("FAIL")





# 3. IF-ELIF-ELSE ladder - Most important
percentage = 75

if percentage >= 90:
    print("3. Grade: A+")
elif percentage >= 75:
    print("3. Grade: A - Excellent!")
elif percentage >= 60:
    print("3. Grade: B")
elif percentage >= 35:
    print("3. Grade: Just PASS")
else:
    print("3. Grade: FAIL")





# 4. Nested IF with logical operators
username = "shrutika"
password = 1234

if username == "shrutika":
    if password == 1234:
        print("Login Successful!")
    else:
        print("Incorrect Password")
else:
    print("Incorrect Username")
    




# 5. Small Task - Even or Odd
number = 10
if number % 2 == 0:
    print(f"5. {number} is Even")
else:
    print(f"5. {number} is Odd")