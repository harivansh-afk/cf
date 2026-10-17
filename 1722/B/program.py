def blind(r1, r2):
    same = ["B", "G"]

    result = bool

    for i in range(len(r1)):
        if (r1[i] != r2[i]) or (r1[i] and r2[i] not in same):
            result = False

    print(result)



t = int(input())

for _ in range(t):
    c = int(input())
    r1 = input()
    r2 = input()

    blind(r1, r2)
