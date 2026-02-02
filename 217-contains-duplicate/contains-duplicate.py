class Solution(object):
    def containsDuplicate(self, nums):
        seen={}
        for num in nums:
            if num in seen:
                return True
            seen[num]=1
        return False
        


        """
        :type nums: List[int]
        :rtype: bool
        """
        