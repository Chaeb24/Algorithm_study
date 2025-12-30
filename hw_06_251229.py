N, L = map(int, input().split())

for i in range(L, 101):
    ix = N - (i * (i + 1) // 2) # 등차수열 공식
    if ix % i == 0: # x가 정수인지 확인
        x = ix // i
        if x + 1 >= 0:
            print(*(i for i in range(x + 1, x + i + 1)))
            break
else:
    print(-1)
