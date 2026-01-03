T = int(input()) #테스트 케이스

for _ in range(T):
    A,B = map(int,input().split()) #업무개수
    A %= 10

    if A == 0:
        print(10)
        continue

    # 일의 자리 패턴
    cycle = []
    for i in range(1, 5):
        cycle.append((A ** i) % 10)

    print(cycle[(B-1) % 4])



