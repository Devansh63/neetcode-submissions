class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)

        mink = r
        
        while l<=r:
            time = 0
            k = (l+r)//2
            for p in piles:
                time += math.ceil(float(p)/k)
            if time<=h:
                mink = k
                r = k-1
            else:
                l = k+1
        
        return mink


        