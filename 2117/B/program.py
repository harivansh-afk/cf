def shrink(n):
    a = [1]
    for i in range(3,n+1):
        a.append(i)
    a.append(2)

    print(*a)


t = int(input())

for _ in range(t):
    n = int(input())
    shrink(n)
