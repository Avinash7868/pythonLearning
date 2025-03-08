l1 = ["avi",False,2,4450.00]

# Append an element to the list
l1.append("new_element")

# Insert an element at a specific position
l1.insert(1, "inserted_element")

# Remove an element from the list
l1.remove(False)

# Pop an element from the list
popped_element = l1.pop(2)

# Get the index of an element
index_of_avi = l1.index("avi")

# Count occurrences of an element
count_of_avi = l1.count("avi")

# Sort the list (will raise an error due to mixed types)
# l1.sort()

# Reverse the list
l1.reverse()

# Print the modified list and other results
print(l1)
print(popped_element)
print(index_of_avi)
print(count_of_avi)