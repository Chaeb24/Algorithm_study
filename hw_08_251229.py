T = int(input()) # 테스트 케이스 개수

queue = []
visited = [] # 방문 여부 체크
for _ in range(T):
    data = input().split()  # 몇 개가 오든 리스트로 저장
    queue.append(data)

def bfs(queue,visited):
    count = 0 # 친구 몇 명인지 세기
    for _ in range(1,3): # 2번째 친구까지만 확인
        a = queue.pop()
        visited.append(a)
        visited[a] = True
        count += 1
        if not visited[a]:
            bfs(queue, visited)
    print(count)

bfs(queue, visited)



