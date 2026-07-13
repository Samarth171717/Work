class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)  # Append a zero height to ensure we pop all elements from the stack at the end
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                popped=stack.pop()
                height = heights[popped]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                area = height * width
                max_area = max(max_area, area)
            stack.append(i)
        return max_area