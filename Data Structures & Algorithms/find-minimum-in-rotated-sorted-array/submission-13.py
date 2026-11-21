class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:          # this window is already sorted
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])        # remember m before skipping it
            if nums[m] >= nums[l]:         # m is in the left sorted part
                l = m + 1                  # so the min is to the right
            else:                          # m is in the right sorted part
                r = m                  
        return res
            


            



        