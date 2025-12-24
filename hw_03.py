def dfs(cnt):
    global answer

    if cnt == B: # cnt 더하다가 교환횟수 도달 시
        answer = max(answer, int("".join(nums)))
        return

    key = ("".join(nums), cnt)
    if key in visited:
        return
    visited.add(key)

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            dfs(cnt + 1)
            nums[i], nums[j] = nums[j], nums[i]


T = int(input())
for tc in range(1, T + 1):
    num, B = input().split()
    B = int(B) # 교환 횟수

    nums = list(num)
    visited = set() # 방문 여부 표시
    answer = 0

    dfs(0)

    print(f"#{tc} {answer}")
