class Solution(object):
    def intersection(self, nums1, nums2):
        set1=set(nums1)
        result=set()
        for num in nums2:
            if num in  nums1:
                result.add(num)
        return list(result)
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        