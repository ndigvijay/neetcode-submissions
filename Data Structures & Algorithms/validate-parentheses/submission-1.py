class Solution:
    def isValid(self, s: str) -> bool:
        valid_params ={ "}":"{","]":"[",")":"("}
        param_list = []
        for i in s:
            if i =="{" or i == "(" or i =="[":
                param_list.append(i)
            else:
                if len(valid_params) > 0 and valid_params[i] != param_list[-1]:
                    return False
                param_list.pop()
                
        return True

        