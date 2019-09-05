print("Problem 1")

myList = [44, 21, 52]

counter = 0
total = 0
for x in myList: 
    total += x
    counter += 1

print(total)
print(" ")
print("Problem 2")

largeNum = [44, 56, 181, 45, 1]

count = 0
largestNum = largeNum[0]
for x in largeNum: 
    if largeNum[count] > largestNum: 
        largestNum = x
    count += 1 
print(largestNum)

print(" ")
print("Problem 3")

aSmall = [44, 56, 181, 45, 1]
count = 0
smallestNum = aSmall[0]
for x in aSmall: 
    if aSmall[count] < smallestNum: 
        smallestNum = x
    count += 1 
print(smallestNum)

print(" ")
print("Problem 4")

aList = [3, 88, 65, 66, 13, 18, 7]

count = 0
evensList =[]
for x in aList: 
    if x % 2 == 0: 
        evensList.append(x)
print(evensList)

print(" ")
print("Problem: Multiply a List")

makeBig = [4, 61, 20, 5]

count = 0
makeBigger = []
for x in makeBig: 
    makeBigger.append(x * 2)
print(makeBigger)

listA = [4, 6, 8]
listB = [5, 9, 10]

count = 0
combinedList = []
for x in listA: 
    combinedList.append(listB[count] * x)
    count += 1
print(combinedList)

# oneMatrix = [[3,4],[5,8]]
# twoMatrix = [[4,4],[1,6]]
# index = 0
# newMatrix = []
# for x in oneMatrix: 
#     y = 0
#     for y in x: 
#         y += twoMatrix[x][y]
#         y += 1
#     index += 1
# print(newMatrix)


