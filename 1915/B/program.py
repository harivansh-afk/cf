def latin(s) -> None:
    if s.count("A") == 2:
        print("A")
    elif s.count("B") == 2:
        print("B")
    else:
        print("C")


t = int(input())

for _ in range(t):
    s = str()
    for i in range(3):
        s += input()

    latin(s)
