c=int(input())
a=c//3600
b=c%3600//60
c=c%60
print(f'{a:02}:{b:02}:{c:02}',end='')