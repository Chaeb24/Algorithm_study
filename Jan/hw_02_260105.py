N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
A.sort() # 오름차순
B_sorted = sorted(B,reverse=True) #내림차순

for i in range(N):
    answer += A[i] * B_sorted[i]

print(answer)
    
