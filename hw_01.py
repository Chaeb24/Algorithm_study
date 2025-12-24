N = 10 # test case 수

for i in range(1,N+1):
    M = int(input())
    arr = list(map(int, input().split()))
    for j in range(M):
        valueMax = max(arr)
        valueMin = min(arr)
        minIndex = arr.index(valueMin)
        maxIndex = arr.index(valueMax)
        arr[minIndex]+=1
        arr[maxIndex]-=1
    answer = max(arr) - min(arr)
    print(f"#{i} {answer}")
    
    