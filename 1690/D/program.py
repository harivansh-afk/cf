def strips(n,k,s) -> None:
    count = s[:k].count('W')
    best = count

    for i in range(k,n):
        if s[i-k] == 'W':
            count -= 1

        if s[i] == 'W':
            count += 1

        if count < best:
            best = count

    print(best)

t = int(input())

for _ in range(t):
    n,k = list(map(int, input().split()))
    s = input()
    strips(n,k,s)
