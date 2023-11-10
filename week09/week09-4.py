a=list(map(int,input().split()))#斷開，整數，變list
ans=a[0]#取最前面數字
for x in a:#把所有數字巡一次
  if x>ans:#如果比現在ans大
    ans=x#更新答案
print('最大值是:',ans)#離開迴圈時便找到ans
for x in a:
  print(x)