class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i,j = 0,n-1
        maxi = 0
        while i < j:
            length = j-i
            height = min(heights[i],heights[j])
            area = length*height
            # print(area)
            maxi = max(area,maxi)
            if heights[i]<heights[j]:
                i += 1
            else:
                j -= 1
        return maxi

