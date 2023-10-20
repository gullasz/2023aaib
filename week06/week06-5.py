class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for c in s:
            if c in d:
               d[c]=d[c]+1
            else:
                 d[c]=1
            #print(d) #可以印印看 字母出現在次數統計結果

        for c in t:
            if c not in d: #沒出現
                return c   #找出多出字母
            if d[c]==0:    #字母用光不夠用 就是他
                return c   #找出多出字母
            else:
                d[c]=d[c]-1 #簡單的減掉1
        return ''            #不寫沒關係 題目保證在前面一定能找到