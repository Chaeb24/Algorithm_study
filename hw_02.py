T = int(input())
for test_case in range(1, T + 1):
    X = int(input())
    if X % 2 == 0:
        print("8"*(X//2))
    elif X == 1:
        print("0")
    else:
        print('4',end="")
        print("8"*(X//2))
            
    