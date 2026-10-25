def atilla(s) -> None:
    alphabets = "abcdefghijklmnopqrstuvwxyz"
   
    max = 0

    for i in range(len(s)):
        index = alphabets.find(s[i]) + 1
        if index > max:
            max = index

    print(max)

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    atilla(s)
