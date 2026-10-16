def prefix(n, arr) -> int:
    b = (max(arr)*n)
    print(b)
    return(b)


t = int(input())

for _ in range(t):
    n = int(input())
    arr = map(int, input().split())
    prefix(n,arr)
