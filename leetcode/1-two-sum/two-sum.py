class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            sub=target-nums[i]
            if sub in nums:
                a=nums.index(sub)
                if(a!=i):
                    return i,a



        