a=12345
ans=0
while a>0: #ans抬升10倍加上個位數的a%10
  ans=ans*10+a%10
  print('現在a:',a,'現在a%10:',a%10,'現在ans:',ans)
  a=a//10 #最後面才能撥掉皮
print('ans:',ans)