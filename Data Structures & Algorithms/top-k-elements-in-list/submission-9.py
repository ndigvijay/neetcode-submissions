class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        k_freq_dict ={}
        for i in nums:
            if i not in k_freq_dict:
                k_freq_dict[i] = 1
            else:
                k_freq_dict[i] = k_freq_dict[i] +1
        print(k_freq_dict)
        k_fre_dict = sorted(k_freq_dict.items(),key=lambda x:x[1],reverse=True)
        numbers = list(k_freq_dict.keys())
        print(numbers)
        return numbers[-k:]
        # for i in range(k,)




        
        