a=int(input())
for i in range(a):
	for j in range(a-1-i):
		print(' ',end='')
	for i in range(2*i+1):
		print('*',end='')
	print()