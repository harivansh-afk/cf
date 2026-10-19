def skibidus(s) -> None:
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            print(1)
            return

    print(len(s))


t = int(input())

for _ in range(t):
    s = input()
    skibidus(s)
