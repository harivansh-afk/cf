def strips(n,k,s) -> None:
    arr = [] 
    for i in range(n-k+1):
        arr.append(s[i:i+k])

    best = min(arr, key=lambda b:b.count('W'))

    print(best.count('W'))


t = int(input())

for _ in range(t):
    n,k = list(map(int, input().split()))
    s = input()
    strips(n,k,s)
