from collections import Counter
import sys

def triple(arr) -> None:

    hm = Counter(arr)

    for i in hm:
        if hm[i] >= 3:
            print(i)
            return
    print(-1)

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int,  sys.stdin.readline().split()))
    triple(arr)
