class Solution:
    def maxScore(self, s: str) -> int:
        N=len(s)
        ans=0
        for left in range(N-1):#減留給右邊
            #...left  left+1....N-1 左邊有幾個0 右邊有幾個1
            now=0 #現在答案
            for i in range(N):
                if i<=left and s[i]=='0':now+=1
                if i>left and s[i]=='1' :now+=1
            if now>ans:ans=now
        return ans