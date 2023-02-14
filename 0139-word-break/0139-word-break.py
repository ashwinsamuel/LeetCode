class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        class TrieNode:
            def __init__(self):
                self.child = {}
                self.word = False
                
        def insert(root,word):
            curr=root
            for ch in word:
                if ch not in curr.child:
                    curr.child[ch]=TrieNode()
                curr=curr.child[ch]
            curr.word=True

        def match(root,s,dp,start):
            curr=root
            for i,ch in enumerate(s[start:]):
                if ch not in curr.child:
                    if curr.word:
                        if start+i not in dp:
                            dp[start] = match(root,s,dp,start+i)
                            return dp[start]
                        else:
                            dp[start] = dp[start+i]
                            return dp[start]
                    else:
                        dp[start]=False
                        return False
                else:
                    if curr.word:
                        if start+i not in dp:
                            tans = match(root,s,dp,start+i)
                        else:
                            tans = dp[start+i]
                        if tans:
                            dp[start]=True
                            return True
                    curr=curr.child[ch]
            
            dp[start]=curr.word
            return dp[start]
        
        root = TrieNode()
        for word in wordDict:
            insert(root,word)
    
        dp={}
        return match(root,s,dp,0)