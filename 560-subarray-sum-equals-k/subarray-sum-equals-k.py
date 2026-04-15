class Solution(object):
    def subarraySum(self, nums, k):
        prefix_map={0:1}
        current_sum=0
        count=0
        for num in nums:
            current_sum+=num
            if current_sum-k in prefix_map:
                count+=prefix_map[current_sum-k]
            prefix_map[current_sum]=prefix_map.get(current_sum,0)+1
        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        