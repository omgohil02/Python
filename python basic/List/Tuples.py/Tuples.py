# Creating tuples
point = (3, 4)
single = (1,) # Note the comma!
empty = ()
# Basic tuple unpacking
point = (3, 4)
x, y = point
x # 3
y # 4
# Extended unpacking
first, *rest = (1, 2, 3, 4)
first # 1
rest # [2, 3, 4]