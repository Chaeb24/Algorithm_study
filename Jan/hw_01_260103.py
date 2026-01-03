N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]

answer = 64  # 최대 64칸

for x in range(N - 7):
    for y in range(M - 7):
        count_w = 0  # 왼쪽 위가 W일 때
        count_b = 0  # 왼쪽 위가 B일 때

        for i in range(8):
            for j in range(8):
                current = chess[x + i][y + j]

                if (i + j) % 2 == 0:
                    if current != 'W': # W를 기대했는데 아니네
                        count_w += 1
                    if current != 'B': # B를 기대했는데 아니군
                        count_b += 1
                else:
                    if current != 'B':
                        count_w += 1
                    if current != 'W':
                        count_b += 1

        answer = min(answer, count_w, count_b)

print(answer)




    



