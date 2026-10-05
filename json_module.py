import json

# Original Dictionary
my_dict = {"name": "Shubham", "age": 21, "city": "Shevgaon"}
print("Original Dict:", my_dict)




# 1. Dictionary -> JSON String
json_string = json.dumps(my_dict)
print("\n1. Dict to JSON String:", json_string)




# 2. JSON String -> Dictionary
new_dict = json.loads(json_string)
print("\n2. JSON String to Dict:", new_dict)
print("Name:", new_dict["name"])




# 3. Dictionary -> JSON File
with open("data.json", "w") as f:
    json.dump(my_dict, f, indent=4)
print("\n3. Dict to File -> data.json banli")




# 4. JSON File -> Dictionary
with open("data.json", "r") as f:
    file_dict = json.load(f)
print("\n4. File to Dict:", file_dict)