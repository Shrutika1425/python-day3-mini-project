import json
import os

# Original Dictionary
my_dict = {"name": "Shubham", "age": 21, "city": "Shevgaon"}



# 1. Dictionary to JSON String
json_string = json.dumps(my_dict, indent=4)
print("1. Dict to JSON String:\n", json_string)



# 2. JSON String to Dictionary
new_dict = json.loads(json_string)
print("\n2. JSON String to Dict:", new_dict)



# 3. Dictionary to JSON File
with open("data.json", "w") as f:
    json.dump(my_dict, f, indent=4)
print("\n3. File created: data.json")



# 4. JSON File to Dictionary
with open("data.json", "r") as f:
    file_dict = json.load(f)
print("\n4. File to Dict:", file_dict)




# 5. Delete JSON File
if os.path.exists("data.json"):
    os.remove("data.json")
    print("\n5. data.json file deleted!")
else:
    print("\nFile does not exist")