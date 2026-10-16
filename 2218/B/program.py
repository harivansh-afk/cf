def negate(arr) :
    a = arr.pop(arr.index(max(arr)))
    total = 0
    for i in arr:
       total += (-i)
    print(total + a)

t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    negate(arr)
