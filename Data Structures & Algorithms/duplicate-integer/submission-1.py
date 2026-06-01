class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stack = []
        nums.sort()

        for num in nums:
            while stack and num == stack[-1]:
                return True
                break
            stack.append(num)
        
        return False