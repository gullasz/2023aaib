a=[1,3,5,7,9,11,13,15,17,19]
N=len(a)
for i in range(1,N):#迴圈從1開始
    print('檢查',a[i],a[i-1])
    if a[i]-a[i-1]!=a[1]-a[0]: #某兩項相減不等於最前面兩項相減
        print('失敗') #那就是失敗
    #return False
print('檢查結束')    