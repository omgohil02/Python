# Creating Dictionaries
empty = {}
pet = {"name": "Leo", "age": 42}
# Dictionary Operations
pet["sound"] = "Purr!" # Add key and value
pet["age"] = 7 # Update value
age = pet.get("age", 0) # Get with default
del pet["sound"] # Delete key
pet.pop("age") # Remove and return
# Dictionary Methods
pet = {"name": "Frieda", "sound": "Bark!"}
pet.keys() # dict_keys(['name', 'sound'])
pet.values() # dict_values(['Frieda', 'Bark!'])
pet.items() # dict_items([('name', 'Frieda'), ('sound', 'Bark!')])