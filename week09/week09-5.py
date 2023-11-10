class Solution:
    def average(self, salary: List[int]) -> float:
        N=len(salary)-2
        ans=(sum(salary)-max(salary)-min(salary))/N        
        return ans