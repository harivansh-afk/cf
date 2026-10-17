def directions(s):

    startx, starty = (0,0)

    total = []

    for i in s:

        if i == "U":
            starty += 1
        elif i == "D":
            starty -= 1
        elif i == "L":
            startx -= 1
        elif i == "R":
            startx += 1

        total.append([startx,starty])

    if [1,1] in total:
        print("YES")
    else:
        print("NO")


t = int(input())

for _ in range(t):
    l = int(input())
    s = input()
    directions(s)
