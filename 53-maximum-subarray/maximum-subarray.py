class Solution(object):
    def maxSubArray(self, nums):
        current_sum=0
        max_sum=nums[0]
        for num in nums:
            current_sum=current_sum+num
            max_sum=max(max_sum,current_sum)
            if current_sum<0:
                current_sum=0
        return max_sum
        """
        :type nums: List[int]
        :rtype: int
        """
        