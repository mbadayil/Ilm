s="abbcabcbb123456789"
def lengthOfLongestSubstring(self, s):
    s1,s2,len1="","",0
    for i in s:
        if i not in s1:
            s1+=i
        else:
            if len1<len(s1):
                len1=len(s1)
            s1=s1[s1.find(i)+1:]
            s1+=i
            #print(s1,len1)
        if len1<len(s1):
            len1=len(s1)
            s2=s1
    return len1,s2


print(lengthOfLongestSubstring(s,s))
