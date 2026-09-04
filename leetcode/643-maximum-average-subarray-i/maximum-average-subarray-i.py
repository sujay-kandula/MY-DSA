class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left=0
        right=0
        s=0
        avg=0
        max_avg = float('-inf')
        while right<len(nums):
            s+=nums[right]
            if right-left+1==k:
                avg=float(s)/k
                if avg>max_avg:
                    max_avg=avg
                s-=nums[left]
                left+=1
            right+=1
        return max_avg

        