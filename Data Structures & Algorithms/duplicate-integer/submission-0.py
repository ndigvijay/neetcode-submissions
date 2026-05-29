class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers =[]
        for i in nums:
            if i not in unique_numbers:
                unique_numbers.append(i)
            else:
                return True
        return False

        
