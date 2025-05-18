# this is basic in python used in DSA and Development Both
# List
# Dynamic arrays.
# Common operations: indexing, slicing, appending, popping, sorting.
arr = [1, 2, 3, 4, 5]
arr.append(6)
arr.pop()
arr.sort()
arr.reverse()
arr.insert(0, 0)
arr[2] = 1
print(arr)

# Tuples
# Immutable sequences.
# Often used to return multiple values from a function.
point = (2, 3)
x, y = point
print(x, y)

# Sets
# Unordered, no duplicates.
# Fast membership checks.
s = {1, 2, 3, 4, 5}
s.add(4)
s.remove(2)
s.discard(3)
s.update([6, 7, 8])
s.intersection_update([4, 5, 6])
s.difference_update([1, 2, 3])
s.symmetric_difference_update([1, 2, 3])
print(s)
print(len(s))

# Dictionaries
# Key-value pairs.
# Used a lot in hashing problems.
d = {'a': 1, 'b': 2}
d['c'] = 3
print(d)
d['a'] = 4
print(d)
print(d.get('b'))
print(d.get('z', 'Not Found'))
print(d.keys())
print(d.values())
print(d.items())
print(d.pop('a'))
print(d)
print(len(d))
print('a' in d)

# Strings
# Immutable sequences of characters.
# Common operations: indexing, slicing, concatenation, formatting.
s = "Hello, World!"
print(s[0])
print(s[7:12])
print(s.lower())
print(s.upper())
print(s.replace("World", "Python"))
print(s.split(", "))
print(s.join(["Hello", "Python"]))
print(s.find("World"))
print(s.count("o"))
print(s.startswith("Hello"))
print(s.endswith("!"))
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.islower())
print(s.isupper())
print(s.isspace())

# Functions
# First-class citizens.
# Can be passed as arguments, returned from other functions.
def add(a, b):
    return a + b

# Comprehensions
squares = [x*x for x in range(10)]
unique = {x for x in [1, 2, 2, 3]}
mapping = {x: x*x for x in range(3)}
print(squares)
print(unique)
print(mapping)

# collections in python
# Counter
from collections import Counter
counter = Counter("hello world")
print(counter)
print(counter.most_common(2))
print(counter['l'])
# deque/stack
from collections import deque
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()
print(stack)
# queue
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

