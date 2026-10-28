def divide(x,y) -> None:
    if x % y == 0:
        print("Yes")
    else:
        print("no")

t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    divide(x,y)
