def good(n, arr) -> None:
    print(n-min(arr)) 


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    good(n,arr)    
