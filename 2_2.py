A = ['1', '2', '3', '4', '5']

#for i in range(len(A), 1, -1):
#    A[i],A[i-1] = A[i-1],A[i]
#print(' '.join(A))
print(A[len(A) - 1], end = ' ')    
print(' '.join(A[:len(A)-1]), end = ' ')

