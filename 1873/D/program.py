def eraser(n,k,s) -> None:

    count = 0
    i = 0

    while i < n:
        if s[i] == 'B':
            count += 1
            i += k
        else:
            i += 1

    print(count)



t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    s = input()
    eraser(n,k,s)
