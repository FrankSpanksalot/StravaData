import os
def pop(r,c):
    if c % 2 == 0:
        return 8*c+r
    else:
        return 8*(c+1)-1-r 

def printRows(a):
    for row in a:
        print(row)
    print("")
g=[]
os.system("cls")
rows, cols = (8,32)
# arr= [[0]*cols for _ in range(rows)]
# printRows(arr)

arr = [[0 for _ in range(5)] for _ in range(8)]
for r in range(8):
    arr[r][0] =1
    arr[r][4] =1

for r in range(5):
    arr[0][r] = 1
    arr[7][r] = 1
    arr[3][r] =1

for r in range(8):
    for c in range(5):
        if arr[r][c] ==1:
            arr[r][c]= pop(r,c)

def n7():
    arr = [[0 for _ in range(5)] for _ in range(8)]
    for r in range(len(arr)):
        arr[r][0] =1
    for r in range(len(arr[0])):
        arr[0][r] =1
    for r in range(len(arr)-1):
        arr[r+1][1] =1
    for r in range(len(arr[0])-1):
        arr[1][r+1] =1
    arr[0][0]=0
    return arr

def n6():
    arr = [[0 for _ in range(5)] for _ in range(8)]
    for r in range(len(arr)):
        arr[r][0] =1
    for r in range(len(arr)-4):
        arr[r+4][4]=1
    for r in range(len(arr[0])):
        arr[0][r] =1
        arr[4][r] =1
        arr[7][r] =1
    # for r in range(len(arr)-1):
    #     arr[r+1][1] =1
    # for r in range(len(arr[0])-1):
    #     arr[1][r+1] =1
    return arr

def LongTallBar():
    arr = [[1 for _ in range(1)] for _ in range(8)]
    print(arr)
    return arr

printRows(LongTallBar())
