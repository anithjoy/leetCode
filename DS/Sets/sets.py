# In Python, a set is an unordered collection of unique elements. The elements in a set can be of any hashable type, but must be immutable (i.e., their value cannot be changed once they are added to the set).

# Here are some of the most commonly used functions associated with sets in Python:

# Creating a set:
# To create a set in Python, you can use curly braces or the set() function:
# makefile
# Copy code
my_set = {1, 2, 3}
my_set = set([1, 2, 3])
# Adding elements to a set:
# You can add elements to a set using the add() method or the update() method:
# scss
# Copy code
my_set = {1, 2, 3}
my_set.add(4)
my_set.update([4, 5, 6])
# Removing elements from a set:
# You can remove elements from a set using the remove() or discard() method. If the element you are trying to remove is not present in the set, the remove() method will raise a KeyError, whereas the discard() method will do nothing:
# scss
# Copy code
my_set = {1, 2, 3, 4}
my_set.remove(4)
my_set.discard(5)
# Checking membership:
# You can check if an element is in a set using the in keyword:
# bash
# Copy code
my_set = {1, 2, 3}
if 2 in my_set:
    print("2 is in the set")
# Set operations:
# Sets support a number of operations such as union, intersection, difference, and symmetric difference. These operations can be performed using the corresponding methods or operators:
# makefile
# Copy code
set1 = {1, 2, 3}
set2 = {2, 3, 4}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_difference_set = set1.symmetric_difference(set2)
# Other functions:
# There are many other functions associated with sets in Python, such as len() (to get the number of elements in a set), clear() (to remove all elements from a set), and copy() (to create a shallow copy of a set).
# scss
# Copy code
my_set = {1, 2, 3}
print(len(my_set))
my_set.clear()
new_set = my_set.copy()
# Note that sets are mutable, but their elements must be immutable. Also, because sets are unordered, they do not support indexing.