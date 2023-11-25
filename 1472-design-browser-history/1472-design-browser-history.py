class BrowserHistory:

    def __init__(self, homepage: str):
        self.currptr = 1 #current page at (currptr-1)
        self.endptr = 1
        self.pages = [homepage]

    def visit(self, url: str) -> None:
        if self.currptr == len(self.pages):
            self.pages.append(url)
        else:
            self.pages[self.currptr] = url
        self.currptr+=1
        self.endptr = self.currptr

    def back(self, steps: int) -> str:
        self.currptr = max(1,self.currptr-steps)
        return self.pages[self.currptr-1]

    def forward(self, steps: int) -> str:
        self.currptr = min(self.endptr , self.currptr+steps)
        return self.pages[self.currptr-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)