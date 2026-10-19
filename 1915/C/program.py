import math

def square(arr) -> None:
    if str(math.sqrt(sum(arr))).endswith(".0"):
        print("YES")
    else:
        print("NO")


t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    square(arr)
