def perfectroot(n:int):
    for i in range(1, n+1):
        print(i**2, end=' ')
    print()


x = int(input())

for i in range(x):
    y = int(input())
    perfectroot(y)

