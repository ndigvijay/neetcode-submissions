class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_list = []
        for i in nums:
            product = 1
            for j in range(0,len(nums)):
                if i != nums[j]:
                    product = product * nums[j]
            final_list.append(product)
        return final_list
        