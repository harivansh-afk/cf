def cool(n,arr) -> None:
    seg = [arr[0]]
    count = 0
    cur = []
    
    for i in arr:
        cur.append(i)
        if set(seg) <= (set(cur)):
            count += 1
            cur = []
        i += 1

    print(count)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cool(n,arr)
