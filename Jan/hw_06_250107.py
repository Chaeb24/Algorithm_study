s, n, k, r1, r2, c1, c2 = map(int, input().split())

if s == 0: #증가 시간이 0이면 의미 없음
    print(0)
    exit()

def fractal(length,x,y):
    if length == 1:
        return 0
    c = length // n #정사각형을 n 등분
    if c*(n-k)//2 <= x < c*(n+k)//2 and c*(n-k)//2 <= y < c*(n+k)//2:
        return 1
    return fractal(c,x%c,y%c)

for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print(fractal(n**s, i, j), end='')
    print()