T = int(input())

for t in range(T):
    N, M = list(map(int, input().split()))
    if N == 1:
        print(M)
    else:
        numberOne = 1
        numberTwo = 1
        for i in range(N):
            numberOne = numberOne * (M - i)
            numberTwo = numberTwo * (N - i)
        print(numberOne // numberTwo)
    