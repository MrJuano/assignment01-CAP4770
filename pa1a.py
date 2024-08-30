myFlower1 = input()
myFlower2 = input()
myFlower3 = input()

yourFlower1 = input()
yourFlower2 = input()

theirFlower = input()

# Define myList containing myFlower1, myFlower2, and myFlower3 in that order
# Your code here
myList = [myFlower1, myFlower2, myFlower3]

print(myList)

# Define yourList containing yourFlower1 and yourFlower2 in that order
# Your code here
yourList = [yourFlower1, yourFlower2]

print(yourList)

# Define ourList by concatenating myList and yourList
# Your code here
ourList = myList + yourList

print(ourList)

# Append theirFlower to the end of ourList
# Your code here
ourList.append(theirFlower)

print(ourList)

# Replace myFlower2 in ourList with theirFlower
# Your code here
if myFlower2 in ourList:
    i = ourList.index(myFlower2)
    ourList[i] = theirFlower

print(ourList)

# Remove the third element of ourList
# Your code here
ourList.pop(2)

print(ourList)
