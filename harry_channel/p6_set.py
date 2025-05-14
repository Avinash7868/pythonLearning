# Creating a set with curly braces
my_set = {1, 2, 3}

# Creating a set using the set() function
my_set = set([1, 2, 3])

my_set = {1, 2, 3}
my_set.add(4)  # Adds 4 to the set

my_set = {1, 2, 3}
my_set.remove(2)  # Removes 2 from the set; raises KeyError if not found
my_set.discard(3)  # Removes 3 from the set; does nothing if not found

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union: elements in either set
union_set = set1.union(set2)  # {1, 2, 3, 4, 5}

# Intersection: elements in both sets
intersection_set = set1.intersection(set2)  # {3}

# Difference: elements in set1 but not in set2
difference_set = set1.difference(set2)  # {1, 2}

# Symmetric Difference: elements in either set, but not both
symmetric_difference_set = set1.symmetric_difference(set2)  # {1, 2, 4, 5}

my_set = {1, 2, 3}
print(2 in my_set)  # True
print(4 in my_set)  # False

my_set = {1, 2, 3}

# Copying a set
new_set = my_set.copy()

# Clearing a set
my_set.clear()  # my_set becomes an empty set