en_ru = dict()

input = open('en-ru.txt')
s = input.readlines()
for i in s:
	i.lower()
	i.rstrip()
	i.replace('\t-\t', ' ')
	k = i.split()
	if k[0] not in en_ru:
		en_ru[k[0]] = k[2]
input.close()


ru_en = dict()
for key in en_ru:
	ru_en[en_ru[key]] = key
output = open('output.txt', 'w')

#2lazy2sort<FIXME>

for key in ru_en:
	output.write(key)
	output.write(' - ')
	output.write(ru_en[key])
	output.write('\n')
output.close()				
		
