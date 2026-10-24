class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        count = 0

        for ch in s:
            if ch == "(":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    count += 1
                else:
                    top = stack[-1]
                    if ch == ")" and top == "(":
                        stack.pop()

        return count + len(stack)




