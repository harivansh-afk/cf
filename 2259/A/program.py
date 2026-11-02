def moo(n,k,s) -> None:
    total = 0
    for i in range(0,len(s),k):
        if '0' not in s[i:i+k]:
            total += 1

    print(total)


t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    s = input()

    moo(n,k,s)
