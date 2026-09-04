#forloops in python 

#loop through range
for i in range(5):
    print(i)       # 0, 1, 2, 3, 4
    
#loop through collection 
fruits = ["apple", "bannana"]
for fruit in fruits:
    print(fruit)

#with enumerate fro index 
for i, fruit in enumerate(fruits):
    print(f"{i}:{fruit}")
    
#loop control
for i in range(10):
    if i == 3:
        continue   #Skip this intration
    if i == 7:
        break      #exit loop
    print(i)
    
    
#While loops in python 

while True:
    user = input("Enter 'quit' to exit:")
    if user == quit:
        break
    print(f"You entered: {user}")
    