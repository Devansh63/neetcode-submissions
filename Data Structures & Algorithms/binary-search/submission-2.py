class Solution:
    def BinarySearch(self, left: int, right: int, nums:List[int] , target: int) ->int:
       
        if left > right:
            return -1
        middle = left + (right - left) // 2

        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            return self.BinarySearch(middle+1,right,nums,target)

        return self.BinarySearch(left,middle-1,nums,target)

    def search(self, nums: List[int], target: int) -> int:
        return self.BinarySearch(0,len(nums)-1,nums,target)

        