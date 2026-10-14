def sausage(a,b) -> int:
    card = int()
    bank = 1
    
    for i in range(a):
        bank *= 2 
        if b <= a:
            a-=1
        if b > a:
            card += bank
            bank = 1
            a-=1
            b-=1
    print(card)
    return card


x = int(input())

for i in range(x):
    y = input().split()
    z = [int(x) for x in y]
    sausage(z[0], z[1])

