def piles(a, b, c):
    print(max(abs(a - b), abs(a + c - b)))

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    piles(a, b, c)
