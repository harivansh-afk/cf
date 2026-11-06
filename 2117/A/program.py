def alarm(n,x,doors) -> None:
    ones = [i+1 for i in range(n) if doors[i] == 1]
    gap = (max(ones) - min(ones))
    if gap < x:
        print("yes")
    else:
        print("no")
    


t = int(input())

for _ in range(t):
    n,x = map(int, input().split())
    doors = list(map(int, input().split()))
    alarm(n,x,doors)
