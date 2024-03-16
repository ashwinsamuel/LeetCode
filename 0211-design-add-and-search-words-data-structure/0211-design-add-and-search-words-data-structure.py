class WordDictionary:

    def __init__(self):
        Tree = lambda: defaultdict(Tree)
        self. root = Tree()
        

    def addWord(self, word: str) -> None:
        #insert
        curr = self.root
        for ch in word:
            curr = curr[ch]
        curr[0]=True

    def search(self, word: str) -> bool:
        return self.match(word,0,self.root)
    
    def match(self, word, i, node):
        
        if i==len(word):
            return True if 0 in node else False
        
        ch=word[i]
        if ch==".":
            for ch2 in "abcdefghijklmnopqrstuvwxyz":
                if self.match(word, i+1, node[ch2]):
                    return True
            return False
        else:
            if ch in node:
                return self.match(word,i+1,node[ch])
            else:
                return False
                
                    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)