def candies(n, arr) -> None:
    m = min(arr)
    total = int()
    for i in arr:
        total += (i-m)

    print(total)


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    candies(n, arr)
