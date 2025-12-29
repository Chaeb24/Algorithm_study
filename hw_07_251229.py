T = int(input()) # 테스트 케이스 개수

for _ in range(T):
    M, N, K = map(int, input().split()) # 가로길이 M, 세로길이 N, 배추 개수 K
    field = [[0] * M for _ in range(N)] # 배추밭 초기화
    for _ in range(K):
        x, y = map(int, input().split()) # 배추 위치 입력
        field[y][x] = 1 # 배추 심기
    
    visited = [[False] * M for _ in range(N)] # 방문 기록 초기화
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우 이동 방향
    def dfs(x, y):
        stack = [(x, y)]
        visited[y][x] = True
        while stack:
            cx, cy = stack.pop()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if field[ny][nx] == 1 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        stack.append((nx, ny))
    worm_count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                dfs(j, i)
                worm_count += 1
    print(worm_count)