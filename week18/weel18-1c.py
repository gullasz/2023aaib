class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        M='AEIOUaeiou'
        N=len(s)#字串長度     ex:'textbook'
        c=0
        for i in range(N):
            if i<N//2 and s[i] in M:c+=1
            if i>=N//2 and s[i] in M:c-=1
        if c==0:return True
        else:return False