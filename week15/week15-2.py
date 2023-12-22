class Solution:
    def maxScore(self, s: str) -> int:
        N=len(s)
        one=0
        zero=0
        for i in range(N):
            if s[i]=='1':one+=1
        ans=0
        for i in range(N-1):
            if s[i]=='0':
                zero+=1
            if s[i]=='1':
                one-=1
            ans=max(ans,zero+one)
        return ans