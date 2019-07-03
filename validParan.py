l1=[]
l2={"(": ")", "{": "}", "[": "]"}

s="{jhdfjs(sdf(sdfsdf)sdfsdf)sdfsdf[sdf]}"

def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        l1=[]
        l2={"(": ")", "{": "}", "[": "]"}
        count=0
        for i in s:
            if i in "{[(" and i not in l2.values():
                l1.append(i)


            if i in l2.values():
                count+=1
                if l1 and l2:
                    match=l1.pop()
                    if l2[match]==i:
                        count-=1
                    else:
                        return False

        if count==0 and len(l1)==0:
            return True
        return False

print(isValid(s))
        #break
"""
if len(l1)==0:
    print("Perfect", len(l1))
else:
    print("Not balanced2",l1)
"""





"""
class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(dfg)dfg{dfg}[]"))
print(py_solution().is_valid_parenthese("(dfg)[dfg{)dfg}"))
print(py_solution().is_valid_parenthese("(xxcvxcv)"))
"""
