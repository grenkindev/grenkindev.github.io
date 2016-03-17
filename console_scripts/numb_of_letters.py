f1 = open(raw_input('put the name of the exist file:'))
f2 = open(raw_input('put the name of the generated file:'), 'w')
number = raw_input('put number:')

for line in f1:
	if len(line) == int(number) + 1:
		f2.write(line)

f2.close()
f1.close()