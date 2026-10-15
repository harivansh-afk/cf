"""
string s

n lower case Latin letter

char c -> lower case latin letter

one coin -> index 1 <= i <= n

S(i) -> c

- python strings
- how to write correct syntax
- how to break down a problem
- how to understand the problem? -> write it down?
- writing down on top -> not helpful
- use paper/excalidraw to ideate

"""

def palindrome(n:int, s:str, c:str) -> int:
    sum = 0
    def sub(i:str,j:str) -> int:
        if i == j:
            return 0
        elif i == c:
            return 1
        elif j == c:
            return 1
        else:
            return 2

    for x in range(0, n//2):
        sum += sub(s[x],s[n-x-1])

    print(sum)
    return sum


y = int(input())

for i in range(y):
    a, b = input().split()
    a = int(a)
    c = input()
    palindrome(a, c, b)

