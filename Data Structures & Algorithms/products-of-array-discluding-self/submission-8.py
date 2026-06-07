class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        prod = 1
        for n in nums:
            if n == 0:
                zeros+=1
            else:
                prod *= n

        if zeros > 1:
            res = [0] * len(nums)
            return res
        res = [0] * len(nums)
        for i,c in enumerate(nums):
            if zeros: res[i] = 0 if c else prod
            else: res[i] = prod//c
        return res


