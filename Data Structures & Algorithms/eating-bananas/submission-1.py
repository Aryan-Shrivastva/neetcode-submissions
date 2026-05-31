class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = 10**20

        def good(target): #target is k
            hours = 0
            for x in piles:
                hours+=math.ceil(x/target)

            return hours<=h
        


        while left<right:
            mid  = (left+right)//2

            if good(mid):
                right = mid
            else:
                left = mid+1
        return left