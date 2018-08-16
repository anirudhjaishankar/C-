from math import sqrt,floor
def square(a):
    if(sqrt(a) - floor(sqrt(a)) == 0):
        return True
    else:
        return False
def factors(a):
    i = 1
    b = []
    while(i<=sqrt(a)):
        if a%i == 0:
            if a/i == i:
                b.append(i)
            else:
                b.append(i)
                b.append(a/i)
        i += 1
    return b

a = int(input().strip())
b = factors(a)
c = 0
for i in b:
    if(square(i)==False):
        f = 0
        j = 2
        while(j<i):
            if(i%j == 0 and square(j)!=False):
                f+=1
                break
            j += 1
        if(f==0):
            c+=1

print(c)

