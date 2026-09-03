class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res=[]
        curr=[]
        def f(i):
            if i==len(s):
                res.append(" ".join(curr))
                return
            for j in range(i,len(s)):
                word=s[i:j+1]
                if word in wordDict:
                    curr.append(word)
                    f(j+1)
                    curr.pop()
        f(0)
        return res