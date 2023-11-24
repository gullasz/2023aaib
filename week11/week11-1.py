a=30
b=45
ans=0
for i in range(1,a+1):
    if a%i==0 and b%i==0:
        print(i,'可以整除')
        ans=i
print(a,'和',b,'最大公因數是',ans)