class Solution:
    def sort_string(self,string):
        return "".join(sorted(string))
    def groupAnagrams(self, strs: List[str]):
        grouped_anagrams_dictionary = {}
        for i in strs:
            # print(type(i))
            sorted_string = self.sort_string(i)
            # print(sorted_string)
            if sorted_string not in grouped_anagrams_dictionary:
                grouped_anagrams_dictionary[sorted_string] = [i]
            else:
                grouped_anagrams_dictionary[sorted_string].append(i)
        return list(grouped_anagrams_dictionary.values())

        

        # return grouped_anagrams_dictionary.values()

        