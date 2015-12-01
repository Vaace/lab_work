input = open('input.txt', 'r')
output = open('output.txt', 'w')
n = int(input.readline())
a = list(map(int, input.readline().split()))
butt = 0
for i in range(n):
	for j in range(n):
		if a[j] == a[i] and j != i:
			butt = a[i]
print(butt, file = output)
