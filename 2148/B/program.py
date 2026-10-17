def lasers(virt,horiz):
    print(len(virt) + len(horiz))

t = int(input())

for _ in range(t):
    n,m,x,y = map(int, input().split())
    virt = list(map(int, input().split()))
    horiz = list(map(int, input().split()))
    lasers(virt,horiz)

