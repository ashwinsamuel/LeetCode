class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        cnt = Counter()
        for s in arr:
            k = len(s)
            for i in range(k + 1):
                for j in range(i):
                    cnt[s[j:i]] += 1
        ans = []
        for s in arr:
            k = len(s)
            for i in range(k + 1):
                for j in range(i):
                    cnt[s[j:i]] -= 1
            for length in range(1, k + 1):
                v = ''
                for i in range(k - length + 1):
                    if cnt[s[i:i+length]] == 0:
                        if len(v) == 0 or s[i:i+length] <= v:
                            v = s[i:i+length]
                if len(v):
                    ans.append(v)
                    break
            else: ans.append('')
            for i in range(k + 1):
                for j in range(i):
                    cnt[s[j:i]] += 1
        return ans