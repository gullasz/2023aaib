class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1         #一開始是正數
        for n in nums:  #依序取出n
            ans *= n        # 答案 乘 n

        if ans>0: return 1   
        if ans<0: return -1
        if ans==0: return 0