def isSquare(a,b,c,d):
    if a==b==c==d:
        print("YES")
    else:
        print("NO")

x = int(input())

for i in range(x):
    y = input().split()
    isSquare(y[0], y[1], y[2], y[3])


