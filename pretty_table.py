# PrettyTable - Column and Row

import prettytable as pt

# 1. Adding data column
print("--- Adding Column ---")
table1 = pt.PrettyTable()
table1.add_column("Id", [1,2,3,4,5])
table1.add_column("Product Name", ["pen","pencil","notebook","physics Book","Math Book"])
table1.add_column("Price", [10,80,20,150,180])
print(table1)

# 2. Adding data Row
print("\n--- Adding Row ---")
table2 = pt.PrettyTable()
table2.field_names = ["Id", "Product Name", "Price"]
table2.add_row([1, "pen", 10])
table2.add_row([2, "pencil", 80])
table2.add_row([3, "notebook", 20])
table2.add_row([4, "physics Book", 150])
table2.add_row([5, "Math Book", 180])
print(table2)