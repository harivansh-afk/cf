def kiakio(n, arr):
    for _ in range(10):
        for i in range(len(arr)):
            tot = int()
            for j in str(arr[i]):
                tot += int(j)**2

            arr[i] = tot


    seen = {}
    pairs = 0

    for x in arr:
        pairs += seen.get(x,0)
        seen[x] = seen.get(x,0) + 1

    print(pairs)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    kiakio(n, arr)
