class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_freq_dict ={}
        sorted_nums = sorted(nums)
        for i in nums:
            if i not in k_freq_dict:
                k_freq_dict[i] = 1
            else:
                k_freq_dict[i] = k_freq_dict[i] +1
        print(k_freq_dict)
        numbers = list(k_freq_dict.keys())
        return numbers[-k:]
        # for i in range(k,)




        
        