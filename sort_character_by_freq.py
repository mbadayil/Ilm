s="tree"

class Solution:
    def __init__(self):
         pass

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_1=set(s)
        result=""
        s4=()
        while len(s):
            s4=self.longest(s_1,s)
            for i in range((s4[0])):
                result+=s4[1]
            s=s.replace(s4[1],"")
        return result

    def longest(self,s_1,s):
        count=0
        char=""
        for i in s_1:
            if s.count(i)>count:
                count=s.count(i)
                char=i
        return count,char
a=Solution()
print(a.frequencySort(s))
