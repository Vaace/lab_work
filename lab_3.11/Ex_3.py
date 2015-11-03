A = dict()
input = open('input1.txt')
c = input.readlines()
for i in c:
	i = i.rstrip()
	i.replace(',', ' ')
	i.replace('.', ' ')
	i.replace('?', ' ')
	i.replace('!', ' ')
	i.replace('  ', ' ')
	i.lower()		
	e = i.split()
	for j in e:
		if j in A:
			A[j] +=1
		else:
			A[j] = 1
max_n = 0
max_key = ''
for key in A:
	if A[key] > max_n:
		max_n = A[key]
		max_key = key
print(max_key, ': ', max_n, sep = '')		
input.close()	
			
