# Create an empty list
my_list = []

# Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# my_list is now [10, 20, 30, 40]

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)
# my_list is now [10, 15, 20, 30, 40]

# Extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])
# my_list is now [10, 15, 20, 30, 40, 50, 60, 70]

# Remove the last element
my_list.pop()
# my_list is now [10, 15, 20, 30, 40, 50, 60]

# Sort in ascending order
my_list.sort()
# my_list is still [10, 15, 20, 30, 40, 50, 60] (already sorted)

# Find and print the index of 30
index_of_30 = my_list.index(30)
print(f"The index of 30 is: {index_of_30}")