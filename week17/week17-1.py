class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=1
        N=len(nums)#問題長度
        table=[0]*N#放小答案的表格
        table[0]=1#最簡單的問題的答案，只有自己
        for i in range(1,N):#探索更多答案
            table[i]=1#最簡單答案，只有自己
            for k in range(i):#查table[0]....table[i-1]
                if nums[i]>nums[k] and table[k]+1>table[i]:
                    #我比你大可吃你且你答案+我1個，比我原本記下的答案好
                    table[i]=table[k]+1#更新最後最大的答案
            #經過檢查確認table[i]是num[i]對應答案
            if table[i]>ans:ans=table[i]
        return ans
