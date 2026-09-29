class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            width=right-left
            curr_height=min(height[left],height[right])
            area=width*curr_height
            max_area=max(max_area,area)
            if height[left]<height[right]:
                left+=1
            elif height[right]<height[left]:
                right-=1
            else:
                left+=1
        return max_area
