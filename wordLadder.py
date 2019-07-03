def checkv1(word1, word2):
    count=0
    if len(word1)==1:
        if word1 in word2:
            return 0
        else:
            return 1

    for i in word1:
        if i in word2:
            count+=1
    if count==len(word1)-1:
        return count
    else:
        return 0

def ladderLength(self, beginWord, endWord, wordList):
    count=0
    res=[]
    res.append(beginWord)
    if endWord not in wordList:
        return 0
    for word in wordList:
        check1=checkv1(beginWord, word)
        check2=checkv1(endWord, word)
        if check2==0:
            res.append(word)
            res.append(endWord)
            return res

        elif check2==len(word)-1:
            res.append(word)
            print("check2", word)
            res.append(endWord)
            return res
        elif check1==len(word)-1:
            res.append(word)
            print("check1", word)
        beginWord=word
        count=0
    return res


beginWord = "a"
endWord = "c"
wordList = ["a","b","c"]
print(ladderLength(beginWord, beginWord, endWord, wordList))
