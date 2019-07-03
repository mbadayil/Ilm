def twoDisctict(s):
    i=maxLen=0
    j=-1
    for k in range(1,len(s)):
        if s[k]==s[k - 1]:
            continue

        if j >=0 and s[k]!=s[j]:
            maxLen=max(maxLen, k-i)
            i=j+1

        j=k-1

    return max(maxLen, len(s)-i)


print(twoDisctict("ecceeedeeasdsdeeee"))
