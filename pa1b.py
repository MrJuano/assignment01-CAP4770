myFruit1 = input()
myFruit2 = input()
myFruit3 = input()

yourFruit1 = input()
yourFruit2 = input()

theirFruit = input()

# Define a set, fruits, containing myFruit1, myFruit2, and myFruit3
# Your code here
fruits = [myFruit1, myFruit2, myFruit3]

print(sorted(fruits))

# Add theirFruit to fruits
# Your code here
fruits.append(theirFruit)
print(sorted(fruits))

# Find the intersection of fruits, and yourFruit1 and yourFruit2
fruitsInter = [yourFruit1 if yourFruit1 in fruits else yourFruit2 if yourFruit2 in fruits else None]
print(sorted(fruitsInter))

# Remove myFruit1 from fruits
# Your code here
fruits.remove(myFruit1)
print(sorted(fruits))
