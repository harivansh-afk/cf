def minus(n,arr) -> None:
    a,b,c = int(), int(), int()
    for i in arr:
        if i % 4 == 0:
            a += 1
        elif i % 4 == 2:
            b += 1
        elif i == 1:
            c += 1
            

    print(max(a,b,c))
        


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    minus(n,arr)
