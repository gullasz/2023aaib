a=input().split()
N=int(a[0])
ans=0
for i in range(1,N+1):
	ans +=int(a[i])
print(ans)



a=int(input())
print(f'{a}=50*{a//50}+5*{a%50//5}+1*{a%50%5}')



a=int(input())
print(a//7,a%7)