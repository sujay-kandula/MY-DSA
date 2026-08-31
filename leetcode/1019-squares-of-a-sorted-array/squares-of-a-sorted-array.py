class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_num=[]
        for i in range(len(nums)):
            new_num.append(nums[i]*nums[i])
        b=new_num.sort()
        return new_num