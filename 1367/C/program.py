def fit(u) -> int:
    if u <= 0:
        return 0
    return (u+k)//(k+1)


def social(n,k,s) -> None:
    ones = [i for i in range(len(s)) if s[i] == '1']
    count = 0

    if not ones:
        count += fit(n)

    else:
        count += fit(ones[0]-k)
        for j in range(len(ones)-1):
            gap = ones[j+1] - ones[j] - 1
            count += fit(gap-2*k)
        count += fit((n-1-ones[-1])-k)

    print(count)


t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    s = input()
    social(n,k,s)
