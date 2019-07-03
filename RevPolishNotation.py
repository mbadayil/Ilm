l1=["4", "13", "5", "/", "+"]
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        operands = {'+','-','/','*'}
        # Push all alement in a stack, if there is an operand, pop top two elements, compute and push.
        result = 0
        if len(tokens) == 1:
            return int(tokens[0])
        for i in tokens:
            if i in operands:
                y=stack.pop()
                x=stack.pop()

                if i =='+':
                    result=x+y
                elif i == '-':
                    result=x-y
                elif i =='*':
                    result=x*y
                elif i =='/':
                    result = x//y
                stack.append(result)
            else:
                stack.append(int(i))
        return result

a=Solution()
print(a.evalRPN(l1))
