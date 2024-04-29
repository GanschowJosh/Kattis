from math import sqrt

array = [input().split(), input().split(), input().split()]

#convert to ints
for i in range(3):
    for j in range(3):
        array[i][j] = int(array[i][j])
#print(array)

def findNum(arr, num):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == num:
                return i, j

sum = 0
x, y = findNum(array, 1)

for i in range(2, 10):
    currX, currY = findNum(array, i)
    sum += sqrt((abs(currX - x))**2 + (abs(currY - y))**2)
    x, y = currX, currY

print(sum)