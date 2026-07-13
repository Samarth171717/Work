class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for num in nums1:
            idx=nums2.index(num)
            greater=-1
            for j in range(idx+1,len(nums2)):
                if nums2[j]>num:
                    greater=nums2[j]
                    break
            result.append(greater)
        return result