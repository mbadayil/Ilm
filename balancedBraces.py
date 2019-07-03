from pythonds.basic.stack import Stack
s="{}()"

def is_valid_parenthese(s):
    s1={"{":"}","(":")","[":"]"}
    a=Stack
    for i in s:
        if i in "{[(" and i not in s1.values():
            a.push(i)
            if i in s1.values():
                count+=1
                if stack1 and s1:
                    value=a.pop()
                    if s1[value]==i:
                        count-=1
                    else:
                        return False
    if count==0 and len(l1)==0:
        return True
    return False

print(is_valid_parenthese(s))
