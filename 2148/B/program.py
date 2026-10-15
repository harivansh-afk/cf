def lasers(x,y,virt,horiz):
    sum = 0
    for i in virt:
        if i < x:
            sum += 1
    for i in horiz:
        if i < y:
            sum += 1
    print(sum)
    return sum

t = int(input())

for _ in range(t):
    n,m,x,y = map(int, input().split())
    virt = list(map(int, input().split()))
    horiz = list(map(int, input().split()))
    lasers(x,y,virt,horiz)

