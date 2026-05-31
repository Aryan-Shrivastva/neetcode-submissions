class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        left = 0
        right = sum(nums)

        def good(target):
            curr = 0
            count=1

            for x in nums:
                if x>target:
                    return False
                curr+=x
                if curr>target:
                    curr = x
                    count+=1

            return count<=k

        while left<right:
            mid = (left+right)//2

            if good(mid):
                right = mid
            else:
                left = mid+1
        
        return left