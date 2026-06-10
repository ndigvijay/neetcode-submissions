class Solution:
    def binary_search(self,nums,high,low,target):
        if low > high:
            return -1
        mid = (high + low) // 2
        if(nums[mid]== target):
            return mid
        elif nums[mid] > target:
            return self.binary_search(nums,mid-1,low,target)
        else:
            return self.binary_search(nums,high,mid+1,target)
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, len(nums)-1, 0, target)
        