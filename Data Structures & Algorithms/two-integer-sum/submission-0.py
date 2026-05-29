class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_dict = dict()
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference not in check_dict:
                check_dict[nums[i]] = i
            else:
                # value:index
                prev_matching_index = check_dict[difference] # because of line 7
                return [prev_matching_index,i]


        