n = input()

pow = 0

for i in n:
	i = int(i)
	j = i*(10**(4-pow))
	print('[%d]' % j)
	pow = pow +1
