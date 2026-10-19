def skibidus(s) -> None:
    if s.endswith("us"):
        print(s[:-2] + "i")

t = int(input())

for _ in range(t):
    s = input()
    skibidus(s)
