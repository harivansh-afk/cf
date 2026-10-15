def trippi(a:str):
    b = a.split()
    for i in b:
        print(i[0], end='')
    print()

x = int(input())

for i in range(x):
    trippi(input())
