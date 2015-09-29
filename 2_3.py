def check(n):
    m = 0
    for k in range(len(A)):
        if A[k] == n:
            m += 1
    return m       

A = list(map(int, input().split()))
ch = A[0]
for elem in A:
    if check(elem) == 1:
        print(elem, end = ' ')
        
