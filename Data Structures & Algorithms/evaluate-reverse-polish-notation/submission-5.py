class Solution:
    def evaluate_exp(self,num1,num2,op_str):
        if op_str == "+":
            return num1 + num2
        if op_str == "-":
            return num2 - num1
        if op_str == "*":
            return num1 * num2
        if op_str == "/":
            return int(num2 / num1)

    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        operators =["+","-","*","/"]
        for i,v in enumerate(tokens):
            if v not in operators:
                stack.append(v)
            elif len(stack) > 0 and v in operators:
                operand1 = stack.pop()
                operand2 = stack.pop()
                # print(operand1)
                result = self.evaluate_exp(int(operand1),int(operand2),v)
                stack.append(result)
        return int(stack[-1])
                


        
        