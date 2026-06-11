class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # for each possible pair store the area
        # area = min number * the gap
        # return largest area

        i = 0
        j = len(heights) - 1
        mx = 0

        while i < j:
            area = min(heights[i], heights[j]) * (j-i)
            mx = max(area, mx)

            if heights[i] <= heights[j]:
                 i += 1
            else:
                j -= 1

        return mx
            
            





        # mx = max(heights)
        # mx2 = max((x for x in heights if x != mx), default=mx)

        # return int(mx2 * abs(heights.index(mx) - heights.index(mx2)))
