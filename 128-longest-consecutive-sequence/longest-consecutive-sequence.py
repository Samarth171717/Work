class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest=0
        s=set(nums)
        for num in s:
            if num-1 not in s:
                count=1
                while num+1 in s:
                    count+=1
                    num+=1
                longest=max(longest,count)
        return longest
            