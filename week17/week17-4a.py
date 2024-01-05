a=int(input())
t=1
while a>0:
	print(a%10*t,end=' ')
	a=a//10
	t*=10