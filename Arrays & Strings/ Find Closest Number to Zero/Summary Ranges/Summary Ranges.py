class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        
        result = []
        start = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]-1:
                if start == nums[i-1]:
                    result.append(str(start))
                else:
                    result.append(f"({start},{nums[i-1]})")
                
        
sol = Solution()
solution = sol.summaryRanges([0,1,2,4,5,7])
print(solution)
