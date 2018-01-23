# Lists: https://www.hackerrank.com/challenges/python-lists/tutorial

# Tuples: created from arrays, cant be edited

arrayString = ["1", "2", "3", "4"]
arrayInt = [int(x) for x in arrayString]
t = tuple(arrayInt)

print(t)

# List comprehensions:
# [ expression-involving-loop-variable for loop-variable in sequence if boolean-expression-involving-loop-variable ]
# example: ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0]
# https://www.hackerrank.com/challenges/list-comprehensions/tutorial
# example up.

ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0]

# Nested lists: like working with a Matrix, double index access: a[0][1]







