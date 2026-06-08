class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []

        for index,temperature in enumerate(temperatures):
            if len(stack) == 0:
                temperature_tuple = (temperature,index)
                print(temperature_tuple,temperature,index)
                stack.append(temperature_tuple)
                continue
            top = stack[-1]
            print(top,temperature)
            if (temperature > top[0]):
                while(len(stack)>0 and stack[-1][0] < temperature):
                    top = stack[-1]
                    day_difference = index - top[1]
                    index_to_insert = top[1]
                    result[index_to_insert] = day_difference
                    stack.pop()
                    continue
                temperature_tuple = (temperature,index)
                stack.append(temperature_tuple)
            else:
                temperature_tuple = (temperature,index)
                stack.append(temperature_tuple)
        return result
            
                




        