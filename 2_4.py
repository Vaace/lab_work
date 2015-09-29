def check(n):
    m = 0
    for k in range(len(A)):
        if A[k] == n:
            m += 1
    return m       

A = list(map(int, input().split()))
max = 0
n_max = ''
for elem in A:
    if check(elem) > max:
        max = check(elem)
        n_max = elem
print(n_max)        
