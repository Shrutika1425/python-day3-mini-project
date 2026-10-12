# Day 15 - Classes, Objects and Inheritance

# 1. Creating a Class and Object
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def greet(self):
        print(f"Hello {self.name}, welcome to Python")
    
    def __str__(self):
        return f"Hello {self.name}, welcome to python"

# Object creation
u1 = User(1, "omkar")
print(u1)  # __str__ will be called
u1.greet()

u2 = User(2, "Neha")
u2.greet()

# 2. SINGLE INHERITANCE 


# Parent Class
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def display(self):
        print(f"ID: {self.id}, Name: {self.name}")

# Child Class (Single Inheritance)
class Student(Person):  # Student inherits from Person
    def __init__(self, id, name, marks):
        super().__init__(id, name)  # inheriting from parent
        self.marks = marks
    
    def show_marks(self):
        print(f"Marks: {self.marks}")

print("\n--- Single Inheritance Example ---")
s1 = Student(1, "Rohit", 87)
print(s1.id)
print(s1.name)
print(s1.marks)
s1.display()
s1.show_marks()

# 3. MULTIPLE INHERITANCE 


class Engineer(Person):
    def __init__(self, id, name, salary):
        super().__init__(id, name)
        self.salary = salary

print("\n--- Multiple Types from Single Parent ---")
e1 = Engineer(572, "Shivam", 98756)
print(e1.id)
print(e1.name)
print(e1.salary)