number = []
rH = 5
cW = 0
for r in range(rH):
    if cW==0:
        number.append([r,0])
    else:
        for c in range(cW):
            number.append([r,c])

for r in range(3):
    for c in range(2):
        number.append([3,c])


def getMyLight(r,c):
    if c % 2 == 0:
        return 8*c+r
    else:
        return 8*(c+1)-1-r

for r in list(number):
    l = getMyLight(r[0],r[1])
    print(type(l))
    print(f"here   {l}")
