n = int(input())
friends = [input().strip() for _ in range(n)]

answer = 0

for i in range(n):
    visited = [False] * n
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        if friends[i][j] == 'Y':  # 직접 친구
            visited[j] = True
        else:
            # 친구의 친구 체크
            for k in range(n):
                if friends[i][k] == 'Y' and friends[k][j] == 'Y':
                    visited[j] = True
                    break
    cnt = sum(visited)
    answer = max(answer, cnt)

print(answer)
