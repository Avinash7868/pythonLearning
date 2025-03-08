# Creating a dictionary with some initial key-value pairs
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Adding a new key-value pair
my_dict["email"] = "alice@example.com"

# Updating an existing key-value pair
my_dict["age"] = 31

# Accessing a value by its key
print("Name:", my_dict["name"])

# Removing a key-value pair
del my_dict["city"]

# Iterating over the dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking if a key exists in the dictionary
if "email" in my_dict:
    print("Email is present in the dictionary")

# Getting the value of a key with a default value if the key does not exist
phone = my_dict.get("phone", "Not Available")
print("Phone:", phone)

print(my_dict.items())