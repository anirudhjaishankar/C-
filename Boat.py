a = list(map(int,input().split(",")))
b = []
for i in range(a[2]):
    c = list(map(int,input().strip().split(",")))
    b.append(c)
count = 0
for i in range(0,a[0]):
    for j in range(0,a[1]):
        d = []
        for k in range(len(b)):
            di = abs(i - b[k][0])
            dj = abs(j - b[k][1])
            d.append(di+dj)
        d.sort()
        if(len(d)>1 and d[0] in d[1:]):
            count += 1
print(count)

