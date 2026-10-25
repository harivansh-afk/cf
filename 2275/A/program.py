def search(x,y,r) -> None:
    for i in range(-10-r, 10+r):
        for j in range(-10-r,10+r):
            if (x-i)**2 + ((y-j)**2) == r**2:
                print(i,j)
                return
            j+=1
        i+=1



t = int(input())

for _ in range(t):
    x,y,r = map(int, input().split())
    search(x,y,r)
