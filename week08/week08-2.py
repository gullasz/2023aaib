a=[1,3,5,7,9,11,13,15,17,19]
for i in range(7):
    print('第i個數字是',a[i])
print('上面的迴圈不好，下面的才能全部照顧到')
N=len(a) #先知道有幾個數字 a陣列的長度(length)
for i in range(N): #才能在for迴圈裡得到正確的range 
    print('第i個數字是',a[i])