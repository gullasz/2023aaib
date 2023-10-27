a=int(input())
c=a
b=0
while c>0:
	b=b*10+c%10
	c=c//10
print(f'{a}+{b}={a+b}')	