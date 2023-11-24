#輾轉相除法
a=123456789012354
b=98765432101849
def gcd(a,b):#定義函式
    print(a,b)#過程
    if a==0:return b#終止條件 遇到0另一邊是答案
    if b==0:return a#終止條件 遇到0另一邊是答案
    return gcd(b,a%b)#函式呼叫函式直到成功
ans=gcd(a,b)#答案
print(ans)