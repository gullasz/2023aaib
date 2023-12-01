class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0 
        while n>0: #剝皮法 一次剝一層
            ans+=n%2 #剝下來的收起來
            n=n//2 #剝皮後變小
        return ans