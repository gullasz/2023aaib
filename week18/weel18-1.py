class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        MA=0#A的母音數
        MB=0#B的母音數
        N=len(s)#字串長度     ex:'textbook'
        a=s[:N//2]#前半段     ex:'text'  
        b=s[N//2:]#後半段     ex:'book'
        for c in a:
               if c=='a'or c=='e'or c=='i'or c=='o'or c=='u'or c=='A'or c=='E'or c=='I'or c=='O'or c=='U':
                   MA+=1
        for c in b:
               if c=='a'or c=='e'or c=='i'or c=='o'or c=='u'or c=='A'or c=='E'or c=='I'or c=='O'or c=='U':
                   MB+=1
        if MA==MB: return True
        else:return False
        