def distinct(n, arr):
    u = len(set(arr))
    d = len(arr)-u

    if d%2 == 0:
        print(u)
    else:
        print(u-1)


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    distinct(n,arr)
