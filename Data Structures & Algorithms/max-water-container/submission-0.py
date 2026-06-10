class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1
        max_area = 0
        while(start<end):
            width = end - start
            height = min(heights[start],heights[end])
            area = width * height
            if area > max_area:
                max_area = area
            start = start + 1
        return max_area

        