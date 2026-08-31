class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        nums=[]
        for i in range(left,right+1):
            num=i
            status=False
            while num!=0:
                digit=num%10
                if digit==0 or i%digit!=0:
                    break
                else:
                    num=num//10
                if num==0:
                    status=True
            if status==True:
                nums.append(i)
        return nums

                