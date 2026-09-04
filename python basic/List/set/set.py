# Creating Sets
a = {1, 2, 3}
b = set([3, 4, 4, 5])
# Set Operations
a | b # {1, 2, 3, 4, 5}
a & b # {3}
a - b # {1, 2}
a ^ b # {1, 2, 4, 5}