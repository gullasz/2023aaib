a=int(input())
if a<=1500:print(100,end='')
else:
	print(100+(a-1500+249)//250*5,end='')