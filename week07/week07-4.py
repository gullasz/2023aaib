class Solution:
    def isPowerOfTwo(self, n: int) -> bool:        
        if n<=0: return False    #負的為錯            
        while  n>1:   #檢查
            if n%2 !=0:
                return False #失敗   
            n=n//2
        return True #成功                           