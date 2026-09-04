class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        new_l=[]
        for i in range(len(nums)):
            new_l.append(nums[i])
            max1=max(new_l)
            min1=min(nums[i:len(nums)])
            ans=max1-min1
            if ans<=k:
                return i
        return -1