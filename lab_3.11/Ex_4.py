en_ru = dict()

input = open('en-ru.txt')
s = input.readlines()
for i in s:
	i.lower()
	i.rstrip()
	i.replace('	-	', ' ')
	k = i.split()
	if k[0] not in en_ru:
		en_ru[k[0]] = k[2]
input.close()
		
input_1 = open('input2.txt')
output = open('output.txt', 'w')
t = input_1.readlines()
for j in t:
	j.lower()
	j.rstrip()
	j.replace(',', ' ')
	j.replace('.', ' ')
	j.replace('?', ' ')
	j.replace('!', ' ')
	j.replace('  ', ' ')
	j.lower()
	n = j.split()
	for x in n:
		if x in en_ru:
			x = en_ru[x]
		output.write(x)
		output.write(' ')
	output.write('\n')
input.close()
output.close()		
			
	
