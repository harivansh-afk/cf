def findreplace(s:str) -> None:
    p1 = ("10"*len(s))[:len(s)]
    p2 = ("01"*len(s))[:len(s)]

    mapp1 = {}
    mapp2 = {}

    result = bool
    
    for i in range(len(s)):
        if s[i] not in mapp1:
            mapp1[s[i]] = p1[i]
        else:
            if p1[i] != mapp1[s[i]]:
                result = False

    for i in range(len(s)):
        if s[i] not in mapp2:
            mapp2[s[i]] = p1[i]
        else:
            if p1[i] != mapp2[s[i]]:
                result = False




    if result:
        print("YES")
    else:
        print('NO')


t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    findreplace(s)
