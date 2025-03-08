# Creating a tuple
my_tuple = ("apple", "banana", "cherry")

# Accessing elements in a tuple
print(my_tuple[0])  # Output: apple
print(my_tuple[1])  # Output: banana
print(my_tuple[2])  # Output: cherry

# Tuples are immutable, so you cannot change their values
# my_tuple[0] = "orange"  # This will raise a TypeError

# You can create a new tuple by concatenating existing tuples
new_tuple = my_tuple + ("orange",)
print(new_tuple)  # Output: ('apple', 'banana', 'cherry', 'orange')

# Tuples can contain different data types
mixed_tuple = (1, "hello", 3.14)
print(mixed_tuple)  # Output: (1, 'hello', 3.14)

# Tuples can be nested
nested_tuple = (my_tuple, mixed_tuple)
print(nested_tuple)  # Output: (('apple', 'banana', 'cherry'), (1, 'hello', 3.14))

# Tuple unpacking
fruit1, fruit2, fruit3 = my_tuple
print(fruit1)  # Output: apple
print(fruit2)  # Output: banana
print(fruit3)  # Output: cherry