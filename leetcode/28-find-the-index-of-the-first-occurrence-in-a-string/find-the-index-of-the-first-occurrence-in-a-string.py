class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n=len(needle)
        m=len(haystack)
        for i in range(m):
            if haystack[i:i+n]==needle:
                return i
        return -1


        