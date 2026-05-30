class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        if target not in nums:
            return -1
        while l<r:

            mid = (l+r)//2

            if target>nums[mid]:
                l = mid+1
            elif target<nums[mid]:
                r = mid
            else:
                return mid
        
        return l