
nmax = 10**6
prime = [True for i in range(nmax+1)]
##SieveOfEratosthenes():
p = 2
while (p * p <= nmax):

    # If prime[p] is not
    # changed, then it is a prime
    if (prime[p] == True):

        # Updating all multiples of p
        for i in range(p * p, nmax+1, p):
            prime[i] = False
    p += 1

primes=[]
for i in range(2,nmax+1):
    if prime[i]:
        primes.append(i)

def factorise(num):
    if prime[num]==True:
        return [num] if num!=1 else []
    ans=[]
    for no in primes:
        while num%no==0:
            num//=no
            ans.append(no)
        if prime[num]==True:
            if num==1:
                return ans
            ans.append(num)
            return ans
    return ans  

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        
        n=len(nums)
        np=len(primes)
        pcnt = {}
        scnt = {}
        pref,suff = 0,0
        for i in range(n):
            ll=factorise(nums[i])
            for p in ll:
                scnt[p]=scnt.get(p,0)+1
        
        
        intrsct = set()
        for i in range(n-1):
            
            ll=factorise(nums[i])
            for p in ll:
                scnt[p]-=1
                pcnt[p]=pcnt.get(p,0)+1
                intrsct.add(p)
                if scnt[p]==0:
                    intrsct.remove(p)
            
            
            if not intrsct:
                return i
            
        return -1
            
            