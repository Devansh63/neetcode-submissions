class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)        
        for i in range(len(nums)):
            out= 1
            for j in range(len(nums)):
                if i == j:
                    continue
                out *= nums[j]    
            output[i] = out
        
        return output