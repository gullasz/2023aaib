class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        notAns=set()
        for a,b in paths:#先巡一次
            notAns.add(a)#出發點不是答案
        
        for a,b in paths:#第二輪，在檢查B
            if b not in notAns:#不再出發裡，就是答案
                return b