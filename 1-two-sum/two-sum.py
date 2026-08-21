class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            compliment=target-nums[i]
            if compliment in seen:
                return [seen[compliment],i]
            seen[nums[i]]=i