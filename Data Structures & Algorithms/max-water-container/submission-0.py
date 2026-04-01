class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max =0
        l=0
        r=len(heights)-1
        while(l<r):
            width = r-l
            maxHeight = min(heights[l], heights[r])
            amount = width * maxHeight
            if(amount > max):
                max = amount
            
            if(heights[l] < heights[r]):
                l+=1
            else:
                r-=1

        return max


        

        
        