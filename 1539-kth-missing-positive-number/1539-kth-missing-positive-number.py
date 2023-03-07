class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def diff(a,i):
            return a-i
        
        n=len(arr)
        if diff(arr[n-1],n)<k: return k - diff(arr[n-1],n) + arr[n-1]
        if diff(arr[0],1)>=k: return k
        
        l,r=0,n-1
        while True:
            mid = (l+r)//2    
            if diff(arr[mid],mid+1) >=k:
                r=mid
            elif diff(arr[mid],mid+1)<k:
                l=mid
            
            if l==r-1:
                break
        
        return k - diff(arr[l],l+1) + arr[l]