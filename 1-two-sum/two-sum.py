class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i in range(len(nums)):
            compliment=target-nums[i]
            if compliment in seen:
                return [seen[compliment],i]
            seen[nums[i]]=i
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        