class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[]
        count1=0
        for _ in s:
            if _ not in l:
                l.append(_)
                if len(l)>count1:
                    count1=len(l)
            else:
                del l[:l.index(_)+1]
                l.append(_)
        return count1