class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxElements=[nums[0]]
        window=[nums[0]]
        
        
        for r in range(1,k):
            if nums[r]>maxElements[0]:
                maxElements[0] = nums[r]
            window.append(nums[r])
        l=k
        
        for r in range(k, len(nums)):
            #dodaj desni
            window.append(nums[r])
            #ukloni levi
            window.pop(0)
            #proveri
            maxElements.append(max(window))
        return maxElements