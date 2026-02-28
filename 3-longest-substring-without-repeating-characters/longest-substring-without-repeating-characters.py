class Solution(object):
    def lengthOfLongestSubstring(self, s):
        num=set()
        left=0
        max_length=0
        for right in range(len(s)):
            while s[right] in num:
                num.remove(s[left])
                left+=1
            num.add(s[right])
            max_length=max(max_length,right-left+1)
        return max_length

        """
        :type s: str
        :rtype: int
        """
        