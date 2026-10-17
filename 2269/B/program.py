def kiakio(n, arr):
    hmap = {}
    for i in arr:
        sum = int()

        for j in str(i):
            sum += int(j)**2


        print(sum)

    print()
                    


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    kiakio(n, arr)
