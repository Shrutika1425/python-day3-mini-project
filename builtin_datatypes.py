# List Methods - Insert, Append, Remove, Changing items, Pop, Clear

my_list = [10, 20, 30]
print("Original List:", my_list)

# append() - adds item at the end
my_list.append(40)
print("After append(40):", my_list)

# insert() - adds item at specific index
my_list.insert(1, 15)
print("After insert(1, 15):", my_list)

# changing items - change value using index
my_list[0] = 100
print("After changing my_list[0] = 100:", my_list)

# remove() - removes first occurrence of value
my_list.remove(15)
print("After remove(15):", my_list)

# pop() - removes item at index (default last)
my_list.pop()
print("After pop():", my_list)

my_list.pop(1)
print("After pop(1):", my_list)

# clear() - removes all items
my_list.clear()
print("After clear():", my_list)




# Creating a tuple
fruits = ("apple", "cherry", "mango", "pineapple")
print(fruits)

# Accessing tuple items
fruits = ("apple", "cherry", "mango", "pineapple")
print(fruits)
print(fruits[2])
print(fruits[1:3])
print(fruits[1:])
print(fruits[:3])

# Changing tuple items

fruits = ("apple", "cherry", "mango", "pineapple")
# tuple --> list --- 1
fruitslist = list(fruits)
# list ---> change --- 2
fruitslist[1] = "grapes"
# list ---> tuple --- 3
fruits = tuple(fruitslist)
print(fruits)

# Adding tuple item - Append
fruits = ("apple", "mango", "banana", "orange", "cherry")
fruitslist = list(fruits)
fruitslist.append("grapes")
fruits = tuple(fruitslist)
print(fruits)

# Insert
names = ("Harshada", "Radhika", "shrutika", "rutuja")
namelist = list(names)
namelist.insert(2, "tanishka")
names = tuple(namelist)
print(names)

# Extend
colors = ("pink", "blue", "purple", "brown")
nums = (12, 13, 25, 14, 17, 20)
colorlist = list(colors)
colorlist.extend(nums)
colors = tuple(colorlist)
print(colors)

# Removing item from tuple list
colors = ("pink", "blue", "purple", "brown")
colorlist = list(colors)
colorlist.remove("brown")
colors = tuple(colorlist)
print(colors)

# Pop method
names = ("shrutika", "radhika", "rutuja", "Harshda")
namelist = list(names)
namelist.pop(1)
names = tuple(namelist)
print(names)

# Clear method
names = ("shrutika", "radhika", "rutuja", "Harshda")
namelist = list(names)
namelist.clear()
names = tuple(namelist)
print(names)

# Sorting # a - z
colors = ("pink", "blue", "purple", "red")
colorlist = list(colors)
colorlist.sort()
colors = tuple(colorlist)
print(colors)

# Sorting # z - a
colors = ("pink", "blue", "purple", "red")
colorlist = list(colors)
colorlist.sort(reverse=True)
colors = tuple(colorlist)
print(colors)

# Increasing
nums = [20, 25, 17, 14]
numslist = list(nums)
numslist.sort()
nums = tuple(numslist)
print(nums)

# Decreasing
nums = (20, 25, 17, 14)
numslist = list(nums)
numslist.sort(reverse=True)
nums = tuple(numslist)
print(nums)

# Copy
names = ("shrutika", "Harshda", "radhika", "rutuja")
namelist = list(names)
new_names = namelist.copy()
names = tuple(namelist)
print(new_names)
print(names)

# Looping
names = ("rutuja", "shrutika", "Harshda", "radhika")
namelist = list(names)
for i in names:
    print(i)
names = tuple(namelist)



## Sets ({})

# Creating a Set
fruits = {"apple", "mango", "banana", "apple", "cherry"}
print(fruits)


# Looping in Set
fruits = {"apple", "mango", "banana", "apple", "cherry"}
for i in fruits:
    print(i)




 
# Creating Dictionary
student = {
    "id": 1,
    "name": "omkar",
    "marks": {
        "maths": 82,
        "physics": 83,
        "chemistry": 84,
        "English": 85
    }
}
print(student)
print(student["id"])
print(student["marks"])
print(student["marks"]["maths"])

# Accessing dictionary items
# method 1
print(student["name"])
# method 2
print(student.get("name"))


# Values method - it will return the list of all the values in the dictionary
print(student.values())


# Keys methods - It will return the list of all the keys from the dictionary
print(student.keys())


# Items methods - It will return us each item in a dictionary as a tuple in a list
print(student.items())


# Changing dictionary items
# ex: method - 1
student["name"] = "omkar Jadhav"
print(student)

# method - 2
student.update({"id": 23})
print(student)

# Adding dictionary items
student = {
    "id": 1,
    "name": "omkar",
    "marks": 85
}
# method - 1
student["age"] = 22
print(student)

# method - 2
student.update({"city": "parphani"})
print(student)

# Removing dictionary items
# 1] Pop - method - it removes the item with specified key name
student = {
    "id": 1,
    "name": "omkar",
    "marks": 85
}
student.pop("id")
print(student)

# 2] Pop-item method - It removes the last inserted item.
student = {
    "id": 1,
    "name": "omkar",
    "mark": 85
}
student.popitem()
print(student)

# Clear method
student = {
    "id": 1,
    "name": "omkar",
    "marks": 85
}
student.clear()
print(student)
# Output: {} - clear whole dictionary

# Copy method
student = {
    "id": 1,
    "name": "omkar",
    "marks": 85
}
students_copy = student.copy()
print(student)
print(students_copy)

# Looping through dictionary
for x in student:
    print(x)  # prints keys

for x in student.keys():
    print(x)

for x in student.values():
    print(x)

for x, y in student.items():
    print(x, y)   