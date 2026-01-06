N = int(input()) #테스트 케이스 수

arr = []
ans = []
for _ in range(N):
    com = input()
    arr.append(com)

for i in range(len(arr[0])):
    same = True
    for j in range(1,N):
        if arr[j][i] != arr[0][i]:
            same = False
            break
    
    if same:
        ans.append(arr[0][i])
    else:
        ans.append("?")

print("".join(ans))