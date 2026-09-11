# Day 05 - Loops 

# 1. For Loop 
for i in range(1, 6):
    print(i)

# 2. For Loop 
fruits = ["apple", "mango", "banana"]
for f in fruits:
    print(f)

# 3. While Loop
count = 1
while count <= 5:
    print(count)
    count = count + 1

# 4. Table of 2
for i in range(1, 11):
    print(2 * i)




    # BREAK 
for i in range(1, 10):
    if i == 5:
        break  # 5 aala ki thambaycha
    print(i)
# Output: 1 2 3 4

print("----")



# CONTINUE 
for i in range(1, 6):
    if i == 3:
        continue  # 3 la skip kar
    print(i)
# Output: 1 2 4 5