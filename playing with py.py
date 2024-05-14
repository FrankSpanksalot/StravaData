from random import randint
l = 37
def findMid(n):
    middle = n/2
    if middle % 2 != 0:
        return int(middle-.5)
    else:
        return int(middle)

color =(1,50,1)

mid =(findMid(l))
np =[(0,0,0)]*l

for p in range(1,mid):
    np[p]  = tuple(x//p for x in color)

for p in range(mid,l):
    np[p] = tuple(x//p for x in color)


def addT(a,b):
    p=a+b
    print(p)

def addT( a,b,c):
    p=a+b+c
    print(p)


addT(1,2,3)

for i in range(34):
    a =  tuple(randint(0,10) for _ in range(3))
    b = tuple(randint(0,10) for _ in range(3))
    print(a,b)