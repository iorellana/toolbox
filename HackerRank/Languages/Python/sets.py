""" Notations
Sets sections of the python track on HackerRank

A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.
"""

s = set()
print(s)

s = set('HackerRank')
print(s)

s = set(['Hacker', 'Rank'])
s = {'Hacker', 'Rank'}
print(s)

s = "1 2 3 4".split()  # Split with no parameters splits by white spacess and generates a list.
print(s)  # Here the numbers are string
s = list(map(int, s))  # Map applies a function to all the elements on the list/set and return it.
print(s)  # Here the numbers are integers.

s = {1, 2, 3, 4}
print(s)
s.add(5)
print(s)
s.add(1)  # Nothing happens cause a set can't have repeated.
print(s)

s.update([1, 2, 3])  # Add several items to the set, only work for interable items.
s.update(['a', 'b', 'c'])  # array
s.update({'d', 'e', 'f'})  # set
s.add((5, 2))  # Tuple
print(s)

s.discard(1)  # Will not raise error if key is not present
try:
    s.remove(1)  # Will raise a KeyError
except KeyError as e:
    print(repr(e))

# Common operations on Sets.
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))  # Not symmetric!








