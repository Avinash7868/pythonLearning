from typing import List, Tuple, Dict, Union, Set

# List of Integers
num_list: List[int] = [2, 34, 54]
print(num_list, "num_list")

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 25)
print(person, "person")

# Dictionary with string keys and integer values
age_dict: Dict[str, int] = {"Alice": 25, "Bob": 30}
print(age_dict, "age_dict")

# Union: A variable that can be an integer or a string
value: Union[int, str] = 42
print(value, "value as int")
value = "Hello"
print(value, "value as string")

# Set of strings
unique_names: Set[str] = {"Alice", "Bob", "Charlie"}
print(unique_names, "unique_names")

# List of Tuples (e.g., coordinates)
coordinates: List[Tuple[int, int]] = [(0, 0), (1, 2), (3, 4)]
print(coordinates, "coordinates")

# Nested Dictionary with typing
nested_dict: Dict[str, Dict[str, int]] = {
    "group1": {"Alice": 25, "Bob": 30},
    "group2": {"Charlie": 35, "Diana": 40},
}
print(nested_dict, "nested_dict")