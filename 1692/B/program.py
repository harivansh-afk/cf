def distinct(n, arr):
    a = len(set(arr))
    if n%2 == 0:
        print(a)
    else:
        print(a-1)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    distinct(n,arr)
