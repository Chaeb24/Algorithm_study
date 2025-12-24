T = int(input())

for test_case in range(1, T + 1):
    A, B, C = map(int, input().split())
 
    volume = A * B * C
     
    if volume % 2 == 0:
        print(1)
    else:
        print(2)
