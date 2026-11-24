class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for val in nums:
            if val in duplicate:
                duplicate[val] += 1
            else:
                duplicate[val] = 1
        
        for key, val in duplicate.items():
            if val > 1:
                return True
        return False

        