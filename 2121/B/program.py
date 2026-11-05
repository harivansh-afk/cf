from collections import Counter

def above(n,s) -> str:
    cnt = Counter(s)

    for i in range(1,n-1):
        if cnt[s[i]] >= 2:
            return "yes"
    return "no"


t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    print(above(n,s))
