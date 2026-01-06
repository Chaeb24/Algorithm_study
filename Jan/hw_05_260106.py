building = int(input())
builds = list(map(int,input().split()))

answer = 0
for i in range(len(builds)):
    count = 0
    # 기준
    x1 = i, y1 = builds[i]
    #왼쪽 기울기
    min_slope = float('inf')
    for j in range(i-1,-1,-1): #인덱스 0까지 줄이기
        slope = (builds[j]-builds[i])/j-i
        if slope < min_slope:
            min_slope = slope
            count += 1
    #오른쪽 기울기
    max_slope = float('inf')
    for j in range(i+1,len(builds)):
        slope = (builds[j]-builds[i])/j-i
        if slope > max_slope:
            max_slope = slope
            count +=1
    answer = max(answer,count)
print(answer)
    