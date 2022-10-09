class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        max_area = 0
        l = 0
        r = len(height) - 1
        while(l < r):
            mini = min(height[l], height[r])
            area = (r-l)*mini
            if area > max_area:
                max_area = area
            
            if mini == height[l]:
                i=l+1
                while(i<r and height[i] < height[l]):
                    i+=1
                l = i
            else:
                i=r-1
                while(i>l and height[i] < height[r]):
                    i-=1
                r = i
        
        return max_area