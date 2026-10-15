def bobritto(n,m,l,r):
    print(l, l+m)    


x = int(input())
for i in range(x):
    a,b,c,d = map(int,input().split())
    bobritto(a,b,c,d)
