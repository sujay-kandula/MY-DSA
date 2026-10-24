class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        openc=0
        closec=0
        for char in s:
            if char=='(':
                openc+=1
            elif openc>0:
                openc-=1
            else:
                closec+=1
        return closec+openc




