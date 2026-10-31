import csv
import os

# 1. WRITE - single rows (tujya vahitla pahila code)
print("1. Creating new_data.csv...")
with open("new_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "Name", "Age"])
    writer.writerow([1, "Omkar", 23])
    writer.writerow([2, "Rohit", 24])
    writer.writerow([3, "Komal", 25])
    writer.writerow([4, "Shivam", 26])


    

# 2. WRITING MULTIPLE ROWS AT A TIME
print("2. Writing multiple rows...")
data = [
    [1, "Rajesh", 20],
    [2, "Vaibhav", 22],
    [3, "Mohan", 21]
]
with open("new_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "Name", "Age"])
    writer.writerows(data)




# 3. APPENDING DATA TO EXISTING CSV
print("3. Appending Harsh...")
with open("new_data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([4, "Harsh", 22])





# 4. READING CSV FILES - using dictionary
print("4. Reading with DictReader...")
students = []
with open("new_data.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)
        print(students)




# 5. READING AND SKIPPING HEADER (products.csv sathi)
# Adhi products.csv banvu
print("\n5. Reading products.csv and skipping header...")
with open("products.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "Name", "Price"])
    writer.writerow([1, "Mobile", 20000])
    writer.writerow([2, "Laptop", 50000])

with open("products.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    for row in reader:
        print(row)




# 6. ACCESSING INDIVIDUAL COLUMNS
print("\n6. Accessing columns...")
with open("products.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print("Name : ", row[1])
        print("Price : ", row[2])
        print()




# 7. FILTERING VALUES
print("7. Filtering Marks > 90...")
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])
    writer.writerow(["Amit", 95])
    writer.writerow(["Rahul", 85])
    writer.writerow(["Sneha", 92])

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["Marks"]) > 90:
            print(row["Name"])



# 8. DELETING CSV FILE (shevti delete karaycha asel tar)
# os.remove("new_data.csv")
# print("File deleted")

print("\nDay 20 Complete - All CSV operations done in one file!")