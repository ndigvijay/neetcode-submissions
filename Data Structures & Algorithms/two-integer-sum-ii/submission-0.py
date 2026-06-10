class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0,len(numbers)-1):
            if numbers[i] + numbers[i+1]==target:
                return [i+1,i+2]
        
        