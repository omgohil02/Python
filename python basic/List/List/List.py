# Creating lists
empty = []
nums = [5]
mixed = [1, "two", 3.0, True]
# List methods
nums.append("x") # Add to end
nums.insert(0, "y") # Insert at index 0
nums.extend(["z", 5]) # Extend with iterable
nums.remove("x") # Remove first "x"
last = nums.pop() # Pop returns last element
# List indexing and checks
fruits = ["banana", "apple", "orange"]
fruits[0] # "banana"
fruits[-1] # "orange"
"apple" in fruits # True
len(fruits) # 3