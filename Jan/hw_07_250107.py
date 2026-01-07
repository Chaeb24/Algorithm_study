N = int(input()) #약수의 개수
arr = list(map(int, input().split())) # 약수 입력, 자기자신과 1 제외

ans = min(arr)*max(arr)
print(ans)