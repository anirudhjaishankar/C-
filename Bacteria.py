# def sumb(a,i,j):
#     print(len(a[0]))
#     if (i == 0):
#         if (j == 0):
#             e = sum(a[i][j + 1] + a[i + 1][j + 1] + a[i + 1][j])
#         elif (j == n[1] - 1):
#             e = sum(a[i][j - 1] + a[i + 1][j - 1] + a[i + 1][j])
#         else:
#             e = sum(a[i][j - 1] + a[i][j + 1] + sum(a[i + 1][j - 1:j + 2]))
#     elif (i == n[0] - 1):
#         if (j == 0):
#             e = sum(a[i][j + 1] + a[i - 1][j + 1] + a[i - 1][j])
#         elif (j == n[1] - 1):
#             e = sum(a[i][j - 1] + a[i - 1][j - 1] + a[i - 1][j])
#         else:
#             e = sum(a[i][j - 1] + a[i][j + 1] + sum(a[i - 1][j - 1:j + 2]))
#     else:
#         if (j == 0):
#             e = sum(a[i + 1][j] + a[i - 1][j] + sum(a[i - 1:i + 2][j + 1]))
#         elif (j == n[1] - 1):
#             e = sum(a[i + 1][j] + a[i - 1][j] + sum(a[i - 1:i + 2][j - 1]))
#         else:
#             e = sum(a[i][j - 1] + a[i][j + 1] + sum(a[i + 1][j - 1:j + 2])) + sum(a[i - 1][j - 1:j + 2])
#     return e

def bacteria(a,n,b,c,d):
    for k in range(d):
        f = []
        for i in range(n[0]):
            g = []
            for j in range(n[1]):
                if(a[i][j]=='1'):
                    if (i == 0):
                        if (j == 0):
                            e = sum(int(a[i][j + 1]) + int(a[i + 1][j + 1]) + int(a[i + 1][j]))
                        elif (j == n[1] - 1):
                            e = sum(int(a[i][j - 1]) + int(a[i + 1][j - 1]) + int(a[i + 1][j]))
                        else:
                            e = sum(int(a[i][j - 1]) + int(a[i][j + 1]) + int(a[i + 1][j - 1])+int(a[i+1][j])+int(a[i+1][j+1]))
                    elif (i == n[0] - 1):
                        if (j == 0):
                            e = sum(int(a[i][j + 1]) + int(a[i - 1][j + 1]) + int(a[i - 1][j]))
                        elif (j == n[1] - 1):
                            e = sum(int(a[i][j - 1]) + int(a[i - 1][j - 1]) + int(a[i - 1][j]))
                        else:
                            e = sum(int(a[i][j - 1]) + int(a[i][j + 1]) + int(a[i - 1][j - 1])+int(a[i-1][j])+int(a[i-1][j+1]))
                    else:
                        if (j == 0):
                            e = sum(int(a[i + 1][j]) + int(a[i - 1][j]) + sum(a[i - 1:i + 2][j + 1]))
                        elif (j == n[1] - 1):
                            e = sum(int(a[i + 1][j]) + int(a[i - 1][j]) + sum(a[i - 1:i + 2][j - 1]))
                        else:
                            e = sum(int(a[i][j - 1]) + int(a[i][j + 1]) + sum(a[i + 1][j - 1:j + 2])) + sum(a[i - 1][j - 1:j + 2])
                    if(e>=b[0] and e<=b[1]):
                        g.append('0')
                    else:
                        g.append('1')
                elif(a[i][j]=='0'):
                    if (i == 0):
                        if (j == 0):
                            e = sum(a[i][j + 1] + a[i + 1][j + 1] + a[i + 1][j])
                        elif (j == n[1] - 1):
                            e = sum(a[i][j - 1] + a[i + 1][j - 1] + a[i + 1][j])
                        else:
                            e = sum(a[i][j - 1] + a[i][j + 1] + sum(a[i + 1][j - 1:j + 2]))
                    elif (i == n[0] - 1):
                        if (j == 0):
                            e = sum(a[i][j + 1] + a[i - 1][j + 1] + a[i - 1][j])
                        elif (j == n[1] - 1):
                            e = sum(a[i][j - 1] + a[i - 1][j - 1] + a[i - 1][j])
                        else:
                            e = sum(a[i][j - 1] + a[i][j + 1] + sum(a[i - 1][j - 1:j + 2]))
                    else:
                        if (j == 0):
                            e = sum(a[i + 1][j] + a[i - 1][j] + sum(a[i - 1:i + 2][j + 1]))
                        elif (j == n[1] - 1):
                            e = sum(a[i + 1][j] + a[i - 1][j] + sum(a[i - 1:i + 2][j - 1]))
                        else:
                            e = sum(a[i][j - 1] + a[i][j + 1] + sum(a[i + 1][j - 1:j + 2])) + sum(a[i - 1][j - 1:j + 2])
                    if (e >= c[0] and e <= c[1]):
                        g.append('1')
                    else:
                        g.append('0')
            f.append(g)
    print(f)
    for i in range(n[0]):
        for j in range(n[1]):
            print(f[i][j],end="")
        print()

t = int(input())
for i in range(t):
    b = []
    n = list(map(int,input().strip().split(" ")))
    for j in range(n[0]):
        m = list(input().strip())
        b.append(m)
    j = list(map(int,input().split(" ")))
    k = list(map(int,input().split(" ")))
    g = int(input())
    bacteria(b,n,j,k,g)


# Example 1
#
# Input
#
# 1
#
# 4 4
#
# 0000
#
# 0110
#
# 0010
#
# 0101
#
# 2 2
#
# 2 3
#
# 3
#
# Output
#
# 0100
#
# 0100
#
# 1110
#
# 0010
# Example 2
#
# Input
#
# 2
#
# 6 6
#
# 000011
#
# 011011
#
# 001011
#
# 011111
#
# 111100
#
# 010101
#
# 2 2
#
# 2 3
#
# 7
#
# 10 4
#
# 0101
#
# 1111
#
# 0000
#
# 0110
#
# 0010
#
# 0101
#
# 1111
#
# 1111
#
# 0000
#
# 0000
#
# 2 2
#
# 2 3
#
# 15
#
# Output
#
# 011100
#
# 100010
#
# 000010
#
# 000001
#
# 111100
#
# 000111
#
# 0110
#
# 1111
#
# 1000
#
# 1011
#
# 0111
#
# 1100
#
# 1110
#
# 1110
#
# 1110
#
# 0000