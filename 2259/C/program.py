def onezeroone(n, a) -> None:

    ones = [i for i in range(n) if a[i] == 1]
    negs = [i for i in range(n) if a[i] == -1]

    cands = []
        
    if not ones:
        if negs:
            cands.append((negs[0], negs[-1]))

    else:
        if negs and negs[0] < ones[0]:
            cands.append((negs[0], ones[0]))

        for k in range(len(ones)-1):
            cands.append((ones[k], ones[k+1]))

        if negs and negs[-1] > ones[-1]:
            cands.append((ones[-1], negs[-1]))

    res = [0 if x == -1 else x for x in a]

    if cands:
        L,R = max(cands, key=lambda c:c[1]-c[0])
        res[L] = res[R] = 1

    print(*res)
    
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    onezeroone(n,a)
