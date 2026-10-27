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
class Student(Person):  
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


# ========== OOPS - Day 15 & 16 ==========



# Day 16 - Multilevel Inheritance

class User2:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Child
class Student(User2):
    def __init__(self, id, name, marks):
        super().__init__(id, name)
        self.marks = marks

# Grand Child
class Engineer(Student):
    def __init__(self, id, name, marks, salary):
        super().__init__(id, name, marks)
        self.salary = salary

e1 = Engineer(1, 'Rohit', 78, 76700)
print(e1.id)
print(e1.name)
print(e1.marks)
print(e1.salary)

# Day 16 - Hybrid Inheritance

# Parent
class A:
    def displayA(self):
        print("class A")

# Child 1
class B(A):
    def displayB(self):
        print("class B")

# Child 2
class C(A):
    def displayC(self):
        print("class C")

class D(B, C):
    def displayD(self):
        print("class D")

obj = D()
obj.displayA()
obj.displayB()
obj.displayC()
obj.displayD()

# Day 16 - Polymorphism


class UserPoly:
    def work(self):
        print("my work is in process")

class StudentPoly:
    def work(self):
        print("my work is study")

class EngineerPoly:
    def work(self):
        print("my work is to build apps")

u1_poly = UserPoly()
s1_poly = StudentPoly()
e1_poly = EngineerPoly()

u1_poly.work()
s1_poly.work()
e1_poly.work()

# Day 16 - Encapsulation

class UserSecure:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

u1_sec = UserSecure(1, "omkar", 20)
print(u1_sec.id)
print(u1_sec.name)
print(u1_sec.get_age())

# Day 16 - OOPS - Abstraction


from abc import ABC, abstractmethod
# abstract class
class UserAbs(ABC):
    # Abstract method
    @abstractmethod
    def work(self):
        pass

class StudentAbs(UserAbs):
    def work(self):
        print("my work is to study")

s1 = StudentAbs()
s1.work()