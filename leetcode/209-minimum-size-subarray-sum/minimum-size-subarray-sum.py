class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if target in nums:
            return 1
        if sum(nums)< target:
            return 0
        left=0
        right=0
        sum1=0
        min_length=len(nums)+1
        while right<len(nums):
            sum1+=nums[right]
            while sum1>=target:
                length=(right-left)+1
                sum1-=nums[left]
                left+=1
                if length<min_length:
                    min_length=length
            right+=1
        return min_length
            
