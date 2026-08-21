class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        if num<10:
            return num
        elif num==0:
            return 0
        else:
            rem=0
            sum1=0
            while(num>0):
                sum1=sum1+num%10
                num=num//10
                if num==0 and sum1>=10:
                    num=sum1
                    rem=0
                    sum1=0
                if num==0 and sum1<10:
                    return sum1
                
               
