def grab(arr: list)-> None:
    odd,even = [], []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    if sum(even) > sum(odd):
        print("YES")
        return
    print("NO")

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    grab(arr)
